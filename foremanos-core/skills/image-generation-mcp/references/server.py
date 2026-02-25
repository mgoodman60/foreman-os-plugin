#!/usr/bin/env python3
"""
Foreman OS Image Generation MCP Server

Provides image generation tools via Flux 2 (Black Forest Labs), Google Gemini,
and a built-in SVG generator. This is a FastMCP server that can be used standalone
or bundled within the Foreman OS plugin.
"""

import os
import json
import base64
import asyncio
import logging
import time
from typing import Optional, Dict, Any, List
from io import BytesIO

import httpx
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("foreman-image-gen")

# Configuration
FLUX2_API_KEY = os.getenv("FLUX2_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

FLUX2_API_BASE = "https://api.bfl.ml/v1"
GEMINI_API_BASE = "https://generativelanguage.googleapis.com/v1beta"

FLUX2_TIMEOUT_SECONDS = 120  # Max time to wait for Flux 2 result
HTTPX_TIMEOUT = 30  # HTTP request timeout
POLL_INTERVAL = 2  # Seconds between Flux 2 status checks
MAX_RETRIES = 5
INITIAL_BACKOFF = 1.0

# Initialize FastMCP server
mcp = FastMCP("foreman-image-gen")


# ============================================================================
# Flux 2 Image Generation (Black Forest Labs)
# ============================================================================

async def _poll_flux2_result(
    client: httpx.AsyncClient,
    task_id: str,
    timeout_seconds: int = FLUX2_TIMEOUT_SECONDS
) -> str:
    """
    Poll Flux 2 API for result until task is complete.

    Args:
        client: httpx async client
        task_id: Task ID returned from initial request
        timeout_seconds: Max seconds to wait

    Returns:
        Image URL when ready

    Raises:
        TimeoutError: If polling exceeds timeout
        Exception: If API returns error status
    """
    start_time = time.time()

    while True:
        elapsed = time.time() - start_time
        if elapsed > timeout_seconds:
            raise TimeoutError(
                f"Flux 2 generation timed out after {timeout_seconds} seconds"
            )

        try:
            response = await client.get(
                f"{FLUX2_API_BASE}/get_result",
                params={"id": task_id},
                timeout=HTTPX_TIMEOUT,
                headers={"x-key": FLUX2_API_KEY}
            )
            response.raise_for_status()
            result = response.json()

            status = result.get("status")
            logger.info(f"Flux 2 task {task_id} status: {status}")

            if status == "Ready":
                image_url = result.get("result", {}).get("sample")
                if not image_url:
                    raise Exception("No image URL in ready response")
                return image_url

            elif status == "Error":
                error_msg = result.get("error", "Unknown error")
                raise Exception(f"Flux 2 generation failed: {error_msg}")

            # Still processing, wait before polling again
            await asyncio.sleep(POLL_INTERVAL)

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                # Rate limited - exponential backoff
                wait_time = 2 ** min(3, int(elapsed / 30))
                logger.warning(f"Flux 2 rate limited, waiting {wait_time}s")
                await asyncio.sleep(wait_time)
            else:
                raise


async def _download_and_encode_image(client: httpx.AsyncClient, url: str) -> str:
    """
    Download image from URL and encode as base64.

    Args:
        client: httpx async client
        url: Image URL

    Returns:
        Base64-encoded image string
    """
    response = await client.get(url, timeout=HTTPX_TIMEOUT)
    response.raise_for_status()
    image_bytes = response.content
    return base64.b64encode(image_bytes).decode('utf-8')


@mcp.tool()
async def generate_image_flux2(
    prompt: str,
    width: int = 1024,
    height: int = 768,
    steps: int = 40,
    guidance: float = 3.5,
    seed: Optional[int] = None,
    output_format: str = "jpeg"
) -> Dict[str, Any]:
    """
    Generate a photorealistic image using Black Forest Labs' Flux 2 model.

    This tool uses an async polling-based API:
    1. Submits generation request and receives task ID
    2. Polls status until image is ready
    3. Downloads and returns base64-encoded image

    Args:
        prompt: Detailed description of the desired image
        width: Image width in pixels (256-2048, default: 1024)
        height: Image height in pixels (256-2048, default: 768)
        steps: Number of diffusion steps (1-100, default: 40)
        guidance: Guidance scale for prompt adherence (1.0-10.0, default: 3.5)
        seed: Optional seed for reproducibility
        output_format: "jpeg" or "png" (default: "jpeg")

    Returns:
        Dictionary with:
            - image_base64: Base64-encoded image data
            - seed_used: Seed value used (for reproducibility)
            - dimensions: {width, height}
            - model: "flux-pro-1.1"
    """
    if not FLUX2_API_KEY:
        raise ValueError(
            "FLUX2_API_KEY environment variable not set. "
            "Get an API key from https://api.bfl.ml/"
        )

    # Validate parameters
    if not 256 <= width <= 2048 or not 256 <= height <= 2048:
        raise ValueError("Width and height must be between 256 and 2048 pixels")
    if not 1 <= steps <= 100:
        raise ValueError("Steps must be between 1 and 100")
    if not 1.0 <= guidance <= 10.0:
        raise ValueError("Guidance must be between 1.0 and 10.0")
    if output_format not in ("jpeg", "png"):
        raise ValueError("Output format must be 'jpeg' or 'png'")

    logger.info(f"Generating Flux 2 image: {prompt[:100]}...")

    # Request payload
    payload = {
        "prompt": prompt,
        "width": width,
        "height": height,
        "steps": steps,
        "guidance": guidance,
        "output_format": output_format
    }
    if seed is not None:
        payload["seed"] = seed

    # Track seed for reproducibility
    used_seed = seed

    try:
        async with httpx.AsyncClient() as client:
            # Step 1: Submit generation request
            logger.info("Submitting Flux 2 request...")
            response = await client.post(
                f"{FLUX2_API_BASE}/flux-pro-1.1",
                json=payload,
                timeout=HTTPX_TIMEOUT,
                headers={"x-key": FLUX2_API_KEY}
            )
            response.raise_for_status()

            request_result = response.json()
            task_id = request_result.get("id")
            if not task_id:
                raise Exception("No task ID in response")

            # Extract seed if returned
            if "seed" in request_result and used_seed is None:
                used_seed = request_result["seed"]

            logger.info(f"Flux 2 task submitted with ID: {task_id}")

            # Step 2: Poll for completion
            image_url = await _poll_flux2_result(client, task_id)

            # Step 3: Download and encode image
            logger.info(f"Downloading image from: {image_url}")
            image_base64 = await _download_and_encode_image(client, image_url)

            logger.info("Flux 2 generation complete")
            return {
                "image_base64": image_base64,
                "seed_used": used_seed,
                "dimensions": {"width": width, "height": height},
                "model": "flux-pro-1.1"
            }

    except httpx.HTTPStatusError as e:
        error_msg = f"Flux 2 API error ({e.response.status_code}): {e.response.text}"
        logger.error(error_msg)
        raise Exception(error_msg)
    except Exception as e:
        logger.error(f"Flux 2 generation failed: {str(e)}")
        raise


# ============================================================================
# Gemini Image Generation (Google)
# ============================================================================

@mcp.tool()
async def generate_image_gemini(
    prompt: str,
    model: str = "gemini-2.0-flash-exp",
    reference_images: Optional[List[str]] = None,
    aspect_ratio: Optional[str] = None
) -> Dict[str, Any]:
    """
    Generate an image using Google Gemini's multimodal capabilities.

    Args:
        prompt: Detailed description of the desired image
        model: Gemini model to use (default: "gemini-2.0-flash-exp")
        reference_images: List of base64-encoded reference images (optional)
        aspect_ratio: Aspect ratio constraint (e.g., "16:9", "1:1", "4:3")

    Returns:
        Dictionary with:
            - image_base64: Base64-encoded image data
            - model_used: Model identifier used
            - dimensions: {width, height} (estimated)
    """
    if not GEMINI_API_KEY:
        raise ValueError(
            "GEMINI_API_KEY environment variable not set. "
            "Get an API key from https://aistudio.google.com/"
        )

    # Build the full prompt with aspect ratio if provided
    full_prompt = prompt
    if aspect_ratio:
        full_prompt = f"{prompt}\n\nGenerate image with aspect ratio {aspect_ratio}."

    logger.info(f"Generating Gemini image: {prompt[:100]}...")

    # Build request content
    content_parts = [
        {
            "text": full_prompt
        }
    ]

    # Add reference images if provided
    if reference_images:
        for i, img_base64 in enumerate(reference_images):
            content_parts.append({
                "inline_data": {
                    "mime_type": "image/jpeg",
                    "data": img_base64
                }
            })
            logger.info(f"Added reference image {i+1}")

    request_payload = {
        "contents": [
            {
                "parts": content_parts
            }
        ],
        "generationConfig": {
            "temperature": 1.0,
            "maxOutputTokens": 1000
        }
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{GEMINI_API_BASE}/models/{model}:generateContent",
                json=request_payload,
                params={"key": GEMINI_API_KEY},
                timeout=HTTPX_TIMEOUT
            )
            response.raise_for_status()

            result = response.json()

            # Extract image from response
            if "candidates" not in result or not result["candidates"]:
                raise Exception("No candidates in Gemini response")

            candidate = result["candidates"][0]
            if "content" not in candidate or "parts" not in candidate["content"]:
                raise Exception("No content in Gemini response")

            # Find the part with inline data (the generated image)
            image_base64 = None
            for part in candidate["content"]["parts"]:
                if "inlineData" in part:
                    image_base64 = part["inlineData"].get("data")
                    break

            if not image_base64:
                # Check if generation was blocked
                if "finishReason" in candidate:
                    reason = candidate["finishReason"]
                    if reason == "SAFETY":
                        raise Exception(
                            "Image generation blocked by safety filter. "
                            "Try a different prompt."
                        )
                raise Exception("No image data in Gemini response")

            logger.info("Gemini image generation complete")

            # Estimate dimensions (Gemini doesn't always return exact size)
            return {
                "image_base64": image_base64,
                "model_used": model,
                "dimensions": {"width": 1024, "height": 1024}  # Estimated
            }

    except httpx.HTTPStatusError as e:
        error_msg = f"Gemini API error ({e.response.status_code}): {e.response.text}"
        logger.error(error_msg)
        raise Exception(error_msg)
    except Exception as e:
        logger.error(f"Gemini generation failed: {str(e)}")
        raise


# ============================================================================
# SVG Generation (Built-in)
# ============================================================================

def _generate_floor_plan_svg(spatial_data: Dict[str, Any], options: Dict[str, Any]) -> str:
    """Generate SVG floor plan from room data."""
    scale = options.get("scale", 1.0)
    show_dimensions = options.get("show_dimensions", True)
    color_scheme = options.get("color_scheme", "default")

    # Color mapping by room type
    colors = {
        "bedroom": "#FFB3B3",
        "bathroom": "#B3D9FF",
        "common": "#B3FFB3",
        "kitchen": "#FFE6B3",
        "office": "#E6D9FF",
        "hallway": "#F0F0F0",
        "mechanical": "#CCCCCC"
    }

    if color_scheme == "bw":
        colors = {k: "#EEEEEE" for k in colors}

    # Calculate canvas size
    max_x = max((r.get("x", 0) + r.get("width", 0)) for r in spatial_data.get("rooms", []))
    max_y = max((r.get("y", 0) + r.get("height", 0)) for r in spatial_data.get("rooms", []))

    width = int((max_x + 20) * scale)
    height = int((max_y + 20) * scale)

    # Build SVG
    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {int(max_x + 20)} {int(max_y + 20)}">',
        '<defs><style>text { font-family: Arial, sans-serif; font-size: 8px; } .dimension { font-size: 6px; }</style></defs>',
        '<rect width="100%" height="100%" fill="white"/>',
    ]

    # Draw grid if requested
    if options.get("include_grid", False):
        for i in range(0, int(max_x) + 20, 10):
            svg_lines.append(f'<line x1="{i}" y1="0" x2="{i}" y2="{int(max_y + 20)}" stroke="#EEE" stroke-width="0.5"/>')
        for i in range(0, int(max_y) + 20, 10):
            svg_lines.append(f'<line x1="0" y1="{i}" x2="{int(max_x + 20)}" y2="{i}" stroke="#EEE" stroke-width="0.5"/>')

    # Draw rooms
    for room in spatial_data.get("rooms", []):
        name = room.get("name", "Room")
        x = room.get("x", 0)
        y = room.get("y", 0)
        w = room.get("width", 0)
        h = room.get("height", 0)
        room_type = room.get("type", "office")
        color = colors.get(room_type, "#FFFFFF")

        # Draw room rectangle
        svg_lines.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'fill="{color}" stroke="#333" stroke-width="1"/>'
        )

        # Draw room label
        svg_lines.append(
            f'<text x="{x + w/2}" y="{y + h/2}" text-anchor="middle" dominant-baseline="middle">'
            f'{name}</text>'
        )

        # Draw dimensions if requested
        if show_dimensions:
            svg_lines.append(
                f'<text class="dimension" x="{x + w/2}" y="{y + h + 8}" text-anchor="middle">'
                f'{w:.0f}x{h:.0f}</text>'
            )

    svg_lines.append('</svg>')
    return '\n'.join(svg_lines)


def _generate_site_plan_svg(spatial_data: Dict[str, Any], options: Dict[str, Any]) -> str:
    """Generate SVG site plan with building, parking, drives, utilities."""
    scale = options.get("scale", 1.0)

    # Get dimensions from spatial_data
    building = spatial_data.get("building", {})
    building_width = building.get("width", 100)
    building_height = building.get("height", 150)
    building_x = building.get("x", 50)
    building_y = building.get("y", 50)

    parking = spatial_data.get("parking", [])
    drives = spatial_data.get("drives", [])
    utilities = spatial_data.get("utilities", [])

    canvas_width = int(300 * scale)
    canvas_height = int(300 * scale)

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_width}" height="{canvas_height}" viewBox="0 0 300 300">',
        '<defs><style>text { font-family: Arial, sans-serif; font-size: 8px; }</style></defs>',
        '<rect width="100%" height="100%" fill="#E8F5E8"/>',  # Grass green
    ]

    # Draw parking areas
    for lot in parking:
        x = lot.get("x", 0)
        y = lot.get("y", 0)
        w = lot.get("width", 50)
        h = lot.get("height", 30)
        svg_lines.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#D3D3D3" stroke="#666" stroke-width="1"/>'
        )
        svg_lines.append(f'<text x="{x + w/2}" y="{y + h/2}" text-anchor="middle">Parking</text>')

    # Draw drives (asphalt gray)
    for drive in drives:
        x = drive.get("x", 0)
        y = drive.get("y", 0)
        w = drive.get("width", 20)
        h = drive.get("height", 100)
        svg_lines.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#555555" stroke="#333" stroke-width="0.5"/>'
        )

    # Draw building
    svg_lines.append(
        f'<rect x="{building_x}" y="{building_y}" width="{building_width}" height="{building_height}" '
        f'fill="#CCCCFF" stroke="#0000AA" stroke-width="2"/>'
    )
    svg_lines.append(
        f'<text x="{building_x + building_width/2}" y="{building_y + building_height/2}" '
        f'text-anchor="middle" dominant-baseline="middle" font-weight="bold">Building</text>'
    )

    # Draw utilities
    for util in utilities:
        x = util.get("x", 0)
        y = util.get("y", 0)
        utility_type = util.get("type", "unknown")
        color = "#FF0000" if utility_type == "electrical" else "#00AAAA"
        svg_lines.append(f'<circle cx="{x}" cy="{y}" r="3" fill="{color}"/>')

    svg_lines.append('</svg>')
    return '\n'.join(svg_lines)


def _generate_grid_svg(spatial_data: Dict[str, Any], options: Dict[str, Any]) -> str:
    """Generate SVG grid visualization."""
    scale = options.get("scale", 1.0)
    show_dimensions = options.get("show_dimensions", True)

    width = spatial_data.get("width", 200)
    height = spatial_data.get("height", 300)
    grid_spacing = spatial_data.get("grid_spacing", 10)

    canvas_width = int(width * scale)
    canvas_height = int(height * scale)

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_width}" height="{canvas_height}" viewBox="0 0 {width} {height}">',
        '<defs><style>text { font-family: monospace; font-size: 8px; }</style></defs>',
        '<rect width="100%" height="100%" fill="white"/>',
    ]

    # Draw grid lines
    for i in range(0, int(width), grid_spacing):
        svg_lines.append(
            f'<line x1="{i}" y1="0" x2="{i}" y2="{height}" stroke="#DDD" stroke-width="0.5"/>'
        )
        if show_dimensions:
            svg_lines.append(f'<text x="{i}" y="10" text-anchor="middle">{i}</text>')

    for i in range(0, int(height), grid_spacing):
        svg_lines.append(
            f'<line x1="0" y1="{i}" x2="{width}" y2="{i}" stroke="#DDD" stroke-width="0.5"/>'
        )
        if show_dimensions:
            svg_lines.append(f'<text x="5" y="{i + 5}" text-anchor="start">{i}</text>')

    # Draw border
    svg_lines.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="none" stroke="black" stroke-width="2"/>')

    svg_lines.append('</svg>')
    return '\n'.join(svg_lines)


def _generate_elevation_svg(spatial_data: Dict[str, Any], options: Dict[str, Any]) -> str:
    """Generate SVG building elevation."""
    scale = options.get("scale", 1.0)
    show_dimensions = options.get("show_dimensions", True)

    width = spatial_data.get("width", 150)
    height = spatial_data.get("height", 100)
    eave_height = spatial_data.get("eave_height", 16)
    roof_slope = spatial_data.get("roof_slope", "1:12")

    canvas_width = int(width * scale)
    canvas_height = int((height + 50) * scale)

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_width}" height="{canvas_height}" viewBox="0 0 {width} {int(height + 50)}">',
        '<defs><style>text { font-family: Arial, sans-serif; font-size: 10px; }</style></defs>',
        '<rect width="100%" height="100%" fill="white"/>',
    ]

    # Foundation
    svg_lines.append(f'<rect x="0" y="{height}" width="{width}" height="10" fill="#8B7355" stroke="#333" stroke-width="1"/>')

    # Walls
    svg_lines.append(f'<rect x="0" y="{height - eave_height}" width="{width}" height="{eave_height}" fill="#D3D3D3" stroke="#333" stroke-width="2"/>')

    # Roof (simple triangle)
    roof_peak_height = height - eave_height - 20
    roof_points = f"0,{height - eave_height} {width/2},{roof_peak_height} {width},{height - eave_height}"
    svg_lines.append(f'<polygon points="{roof_points}" fill="#8B4513" stroke="#333" stroke-width="1.5"/>')

    # Door opening
    door_width = 10
    door_height = 8
    door_x = (width - door_width) / 2
    svg_lines.append(
        f'<rect x="{door_x}" y="{height - door_height}" width="{door_width}" height="{door_height}" '
        f'fill="#A0522D" stroke="#333" stroke-width="1"/>'
    )

    # Dimension lines
    if show_dimensions:
        svg_lines.append(f'<text x="{width/2}" y="{int(height) + 25}" text-anchor="middle">{width:.0f} ft</text>')
        svg_lines.append(f'<text x="-15" y="{int(height - eave_height/2)}" text-anchor="middle">{eave_height:.0f} ft</text>')

    svg_lines.append('</svg>')
    return '\n'.join(svg_lines)


def _generate_isometric_svg(spatial_data: Dict[str, Any], options: Dict[str, Any]) -> str:
    """Generate SVG isometric 3D-ish view of building."""
    scale = options.get("scale", 1.0)

    width = spatial_data.get("width", 100)
    depth = spatial_data.get("depth", 150)
    height = spatial_data.get("height", 80)

    canvas_width = int(400 * scale)
    canvas_height = int(300 * scale)

    # Isometric projection constants
    iso_scale = 2.0
    iso_angle = 30

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{canvas_width}" height="{canvas_height}" viewBox="0 0 400 300">',
        '<defs><style>text { font-family: Arial, sans-serif; font-size: 10px; }</style></defs>',
        '<rect width="100%" height="100%" fill="#F0F0F0"/>',
    ]

    # Draw main box (building) in isometric view
    # Simplified isometric cube representation
    origin_x = 100
    origin_y = 150

    # Front face
    svg_lines.append(
        f'<polygon points="{origin_x},{origin_y} {origin_x + width * iso_scale},{origin_y} '
        f'{origin_x + width * iso_scale},{origin_y - height * iso_scale} {origin_x},{origin_y - height * iso_scale}" '
        f'fill="#B3D9FF" stroke="#333" stroke-width="1.5"/>'
    )

    # Top face
    svg_lines.append(
        f'<polygon points="{origin_x},{origin_y - height * iso_scale} '
        f'{origin_x + width * iso_scale},{origin_y - height * iso_scale} '
        f'{origin_x + width * iso_scale - depth * iso_scale * 0.5},{origin_y - height * iso_scale - depth * iso_scale * 0.25} '
        f'{origin_x - depth * iso_scale * 0.5},{origin_y - depth * iso_scale * 0.25}" '
        f'fill="#E6D9FF" stroke="#333" stroke-width="1.5"/>'
    )

    # Right face
    svg_lines.append(
        f'<polygon points="{origin_x + width * iso_scale},{origin_y} '
        f'{origin_x + width * iso_scale - depth * iso_scale * 0.5},{origin_y - depth * iso_scale * 0.25} '
        f'{origin_x + width * iso_scale - depth * iso_scale * 0.5},{origin_y - height * iso_scale - depth * iso_scale * 0.25} '
        f'{origin_x + width * iso_scale},{origin_y - height * iso_scale}" '
        f'fill="#C0C0C0" stroke="#333" stroke-width="1.5"/>'
    )

    # Label
    svg_lines.append(f'<text x="200" y="30" text-anchor="middle" font-weight="bold">Isometric View</text>')
    svg_lines.append(f'<text x="200" y="280" text-anchor="middle" font-size="9">{width:.0f}x{depth:.0f}x{height:.0f} ft</text>')

    svg_lines.append('</svg>')
    return '\n'.join(svg_lines)


@mcp.tool()
def generate_svg(
    type: str,
    spatial_data: Dict[str, Any],
    options: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Generate construction drawings and diagrams as SVG (vector graphics).

    This tool requires no external APIs and produces publication-ready SVG markup.

    Args:
        type: Drawing type - one of:
            - "floor_plan": Room layout with labels and dimensions
            - "site_plan": Building footprint with parking, drives, utilities
            - "elevation": Building side profile
            - "isometric": 3D-ish isometric view
            - "grid": Reference grid with dimensions
        spatial_data: Data structure defining the space (varies by type)
            - floor_plan: {rooms: [{name, x, y, width, height, type}]}
            - site_plan: {building: {x, y, width, height}, parking: [...], drives: [...], utilities: [...]}
            - elevation: {width, height, eave_height, roof_slope}
            - isometric: {width, depth, height}
            - grid: {width, height, grid_spacing}
        options: Optional rendering settings
            - scale: Scale factor (default: 1.0)
            - show_dimensions: Include dimension labels (default: true)
            - color_scheme: "default", "bw", or "color" (default: "default")
            - include_grid: Show background grid (default: false)

    Returns:
        Dictionary with:
            - svg_string: Valid SVG markup
            - type: Drawing type generated
            - dimensions: {width, height} of canvas
    """
    if options is None:
        options = {}

    logger.info(f"Generating {type} SVG from spatial_data")

    # Dispatch to appropriate generator
    if type == "floor_plan":
        svg_string = _generate_floor_plan_svg(spatial_data, options)
        dimensions = {"width": 500, "height": 500}
    elif type == "site_plan":
        svg_string = _generate_site_plan_svg(spatial_data, options)
        dimensions = {"width": 600, "height": 600}
    elif type == "elevation":
        svg_string = _generate_elevation_svg(spatial_data, options)
        dimensions = {"width": 400, "height": 300}
    elif type == "isometric":
        svg_string = _generate_isometric_svg(spatial_data, options)
        dimensions = {"width": 400, "height": 300}
    elif type == "grid":
        svg_string = _generate_grid_svg(spatial_data, options)
        dimensions = {"width": 300, "height": 400}
    else:
        raise ValueError(
            f"Unknown SVG type: {type}. "
            f"Must be one of: floor_plan, site_plan, elevation, isometric, grid"
        )

    logger.info(f"SVG generation complete ({len(svg_string)} bytes)")

    return {
        "svg_string": svg_string,
        "type": type,
        "dimensions": dimensions
    }


# ============================================================================
# Server Lifecycle
# ============================================================================

async def app_startup():
    """Log startup and available tools."""
    logger.info("=" * 70)
    logger.info("Foreman OS Image Generation MCP Server")
    logger.info("=" * 70)

    available_tools = []

    if FLUX2_API_KEY:
        logger.info("✓ Flux 2 API key detected - generate_image_flux2 available")
        available_tools.append("generate_image_flux2")
    else:
        logger.warning("✗ FLUX2_API_KEY not set - generate_image_flux2 unavailable")

    if GEMINI_API_KEY:
        logger.info("✓ Gemini API key detected - generate_image_gemini available")
        available_tools.append("generate_image_gemini")
    else:
        logger.warning("✗ GEMINI_API_KEY not set - generate_image_gemini unavailable")

    logger.info("✓ SVG generator always available - generate_svg ready")
    available_tools.append("generate_svg")

    logger.info(f"\nAvailable tools: {', '.join(available_tools)}")
    logger.info("Server ready to accept requests")
    logger.info("=" * 70)


if __name__ == "__main__":
    import uvicorn

    # Run FastMCP server
    logger.info("Starting FastMCP server...")
    asyncio.run(app_startup())

    # FastMCP runs on http://localhost:3000 by default
    mcp.run()
