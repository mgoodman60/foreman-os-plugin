---
name: image-generation-mcp
description: >
  MCP server for AI-powered image generation via Flux 2, Google Gemini, and built-in SVG tools. Trigger phrases include "generate image", "create rendering", "make a diagram", "generate SVG", "create visualization".
version: 1.0.0
---

# Image Generation MCP Server

## Overview

The Image Generation MCP server is a FastMCP-based service that provides **three powerful image generation tools** to the Foreman OS plugin. It integrates cutting-edge AI image APIs (Flux 2 and Google Gemini) alongside a lightweight SVG generator for construction drawings, floor plans, and site diagrams.

This server enables the `/render` command in the rendering-generator skill and powers the `/data` dashboard's rendering gallery feature. It is designed as an **optional enhancement**—the plugin functions fully without it, with SVG-based rendering as a fallback.

## What It Does

The Image Generation MCP server exposes three main tools:

### 1. generate_image_flux2
Generates high-quality photorealistic images using Black Forest Labs' Flux 2 model.

**Input Parameters:**
- `prompt` (string, required): Detailed description of the desired image
- `width` (integer, optional): Image width in pixels (default: 1024, range: 256-2048)
- `height` (integer, optional): Image height in pixels (default: 768, range: 256-2048)
- `steps` (integer, optional): Number of diffusion steps (default: 40, range: 1-100)
- `guidance` (float, optional): Guidance scale for prompt adherence (default: 3.5, range: 1.0-10.0)
- `seed` (integer, optional): Random seed for reproducibility (optional)
- `output_format` (string, optional): Output format—`jpeg` or `png` (default: `jpeg`)

**Returns:**
- `image_base64` (string): Base64-encoded image data
- `seed_used` (integer): Seed value used for generation (useful for reproducibility)
- `dimensions` (object): Width and height of generated image
- `model` (string): "flux-pro-1.1"

**Use Cases:**
- Photorealistic renderings of buildings and landscapes
- High-quality marketing and presentation visuals
- Detailed construction site documentation

### 2. generate_image_gemini
Generates images using Google Gemini's multimodal capabilities, with optional image reference inputs.

**Input Parameters:**
- `prompt` (string, required): Detailed description of the desired image
- `model` (string, optional): Gemini model to use (default: "gemini-2.0-flash-exp")
- `reference_images` (array of base64 strings, optional): Reference images to guide generation
- `aspect_ratio` (string, optional): Aspect ratio constraint (e.g., "16:9", "1:1", "4:3", "3:4")

**Returns:**
- `image_base64` (string): Base64-encoded image data
- `model_used` (string): Model identifier that was used
- `dimensions` (object): Width and height of generated image

**Use Cases:**
- Quick concept generation
- Image-to-image transformations with reference images
- Cost-effective batch generation
- Style transfer from reference images

### 3. generate_svg
Pure Python SVG generation without external API calls. Produces vector drawings ideal for construction documents.

**Input Parameters:**
- `type` (string, required): Drawing type—`floor_plan`, `site_plan`, `isometric`, `elevation`, or `grid`
- `spatial_data` (object, required): Data structure defining the space
  - For `floor_plan`: array of room objects `{name, x, y, width, height, type}`
  - For `site_plan`: building footprint, parking areas, drives, utilities
  - For `elevation`: building dimensions and features
  - For `isometric`: 3D spatial data
  - For `grid`: dimension data
- `options` (object, optional): Rendering options
  - `scale` (number): SVG scale factor
  - `show_dimensions` (boolean): Include dimension labels
  - `color_scheme` (string): "default", "bw", or "color"
  - `include_grid` (boolean): Show background grid

**Returns:**
- `svg_string` (string): Valid SVG markup ready for embedding or file export
- `type` (string): Drawing type generated
- `dimensions` (object): Canvas dimensions

**Use Cases:**
- Quick floor plan sketches
- Site layout diagrams
- Architectural elevations
- Construction grid references
- Guaranteed offline rendering (no API dependency)

## Architecture

### Technology Stack
- **Framework:** FastMCP (Anthropic's Model Context Protocol)
- **HTTP Client:** httpx (async HTTP requests)
- **Image Format:** Base64 encoding for integration with LLMs and web platforms
- **SVG Generation:** Pure Python with lxml (structural SVG construction)

### API Integration
- **Flux 2 (Black Forest Labs):** Async polling-based API
  - Initial request returns task ID
  - Poll `GET /get_result?id={id}` until status is "Ready"
  - Download image from result URL and encode to base64
- **Gemini (Google):** Standard synchronous API
  - Single request with inline data handling
  - Supports multimodal inputs (text + images)
- **SVG:** Synchronous Python generation (no external API)

### Error Handling & Resilience
- **Rate Limiting:** Exponential backoff retry logic (max 5 retries)
- **Timeouts:** 30-second timeout on HTTP requests; 2-minute timeout on Flux 2 polling
- **Graceful Degradation:** SVG generation available even if API keys are missing
- **Content Filtering:** Handles Gemini content safety filters
- **Detailed Logging:** All errors logged with context for debugging
- **User-Friendly Messages:** Clear error descriptions returned to client

## Setup Instructions

See `references/setup-guide.md` for complete step-by-step installation and configuration instructions.

### Quick Start
```bash
# 1. Install dependencies
pip install -r references/requirements.txt

# 2. Set environment variables
export FLUX2_API_KEY="your-flux2-key"
export GEMINI_API_KEY="your-gemini-key"

# 3. Run the server
python references/server.py

# 4. Configure in Claude or Foreman OS MCP settings
```

## API Key Requirements

The server uses **optional, modular API keys**:

- **FLUX2_API_KEY:** Required to use `generate_image_flux2`. Get from [Black Forest Labs](https://api.bfl.ml/)
- **GEMINI_API_KEY:** Required to use `generate_image_gemini`. Get from [Google AI Studio](https://aistudio.google.com/)

**Important:** API keys are optional individually. You can:
- Use only Flux 2 (disable Gemini by not setting GEMINI_API_KEY)
- Use only Gemini (disable Flux 2 by not setting FLUX2_API_KEY)
- Use neither (all three tools available, but Flux 2 and Gemini will error if called)
- Use SVG generation without any API keys

The plugin detects available keys at startup and adjusts tool availability dynamically.

## Integration with Foreman OS

### Used By
- **rendering-generator skill:** The `/render` command invokes these tools to generate images for construction documents
- **/data dashboard:** The rendering gallery uses these tools to create visual previews of projects
- **Daily reports:** Image generation for progress documentation

### Environment
The server is designed to run:
- As a standalone FastMCP server in the plugin's runtime environment
- Independently of Foreman OS (can be deployed separately if needed)
- With graceful fallback to SVG when APIs are unavailable

### Tool Availability
Tools are registered only if their dependencies are met:
- `generate_image_flux2`: Registered if FLUX2_API_KEY is set
- `generate_image_gemini`: Registered if GEMINI_API_KEY is set
- `generate_svg`: Always registered (no external dependencies)

## Performance Characteristics

| Tool | Latency | Quality | Cost | Use Case |
|------|---------|---------|------|----------|
| **Flux 2** | 5-15 sec | Photorealistic | Medium | Marketing, renderings |
| **Gemini** | 3-8 sec | Stylized/conceptual | Low | Quick concepts |
| **SVG** | <100ms | Vector/schematic | None | Technical drawings |

## Troubleshooting

### Common Issues

**"API key not found" error**
- Ensure environment variables are exported: `echo $FLUX2_API_KEY`
- Restart the server after setting keys
- Tools won't be available if keys are missing

**Rate limit errors (429)**
- Flux 2 enforces rate limits (e.g., 100 req/min for free tier)
- Server implements exponential backoff; requests will retry automatically
- Check your API tier and usage limits

**Image generation timeout**
- Flux 2 polling timeout is set to 2 minutes per image
- For large/complex prompts, increase `FLUX2_TIMEOUT_SECONDS` in server.py
- Try simpler prompts or smaller dimensions

**SVG generation produces invalid markup**
- Check the `spatial_data` structure matches the expected schema
- See examples in `references/svg_examples.json`

**Gemini content filtering**
- If images are blocked, try reformulating the prompt
- Avoid prompts that might trigger safety filters

## Configuration Options

Advanced settings in `references/server.py`:

```python
# Timeout settings
FLUX2_TIMEOUT_SECONDS = 120  # Max wait for Flux 2 result
HTTPX_TIMEOUT = 30  # HTTP request timeout

# Retry settings
MAX_RETRIES = 5
INITIAL_BACKOFF = 1.0

# Flux 2 polling
POLL_INTERVAL = 2  # seconds between status checks
```

## Development Notes

### Adding New Image Generators
To extend with additional generators (e.g., Midjourney, Stable Diffusion):

1. Create a new `generate_image_<provider>` tool in `server.py`
2. Follow the error handling and logging patterns
3. Add appropriate environment variable checks
4. Update SKILL.md documentation
5. Test graceful degradation if API is unavailable

### Testing
```bash
# Test without API keys (SVG only)
python references/server.py

# Test with Flux 2
export FLUX2_API_KEY="test-key"
python references/server.py

# Verify tools are registered
curl http://localhost:3000/tools  # Adjust port as needed
```

## License & Attribution

- **Flux 2:** Black Forest Labs (https://blackforestlabs.ai/)
- **Gemini:** Google (https://deepmind.google/technologies/gemini/)
- **FastMCP:** Anthropic (https://modelcontextprotocol.io/)

## Support & Documentation

- MCP Specification: https://modelcontextprotocol.io/
- Flux 2 API Docs: https://docs.bfl.ml/
- Gemini API Docs: https://ai.google.dev/
- Setup Guide: See `references/setup-guide.md`
