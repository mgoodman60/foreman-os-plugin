#!/usr/bin/env python3
"""
convert_dwg.py — .dwg to .dxf conversion wrapper

Converts .dwg files to .dxf using the ODA File Converter, then passes
the .dxf through parse_dxf.py for extraction.

If ODA File Converter is not available, provides a clear message
directing the user to request .dxf exports from their architect.

Usage:
    python3 convert_dwg.py <input.dwg> [--output output.json] [parse_dxf options...]
"""

import argparse
import os
import shutil
import subprocess
import sys
import tempfile


def find_oda_converter() -> str:
    """Locate the ODA File Converter binary.

    Returns path to binary, or empty string if not found.
    """
    # Check common installation locations
    candidates = [
        "ODAFileConverter",
        "/usr/bin/ODAFileConverter",
        "/usr/local/bin/ODAFileConverter",
        "/opt/ODAFileConverter/ODAFileConverter",
    ]

    for candidate in candidates:
        if shutil.which(candidate):
            return candidate

    return ""


def convert_dwg_to_dxf(dwg_path: str, oda_binary: str) -> str:
    """Convert a .dwg file to .dxf using ODA File Converter.

    Args:
        dwg_path: Path to input .dwg file
        oda_binary: Path to ODA File Converter binary

    Returns:
        Path to the output .dxf file in a temp directory

    Raises:
        RuntimeError: If conversion fails
    """
    # Create temp directories for ODA (it works with directories, not files)
    input_dir = tempfile.mkdtemp(prefix="dwg_input_")
    output_dir = tempfile.mkdtemp(prefix="dxf_output_")

    try:
        # Copy .dwg to input directory
        dwg_filename = os.path.basename(dwg_path)
        shutil.copy2(dwg_path, os.path.join(input_dir, dwg_filename))

        # ODA File Converter arguments:
        # ODAFileConverter "Input Folder" "Output Folder" version type recurse audit
        # version: "ACAD2018" for R2018 DXF
        # type: "DXF" for DXF output
        # recurse: "0" for no recursion
        # audit: "1" to audit and fix errors
        cmd = [
            oda_binary,
            input_dir,
            output_dir,
            "ACAD2018",  # Output version
            "DXF",       # Output type
            "0",         # No recursion
            "1",         # Audit files
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120  # 2-minute timeout
        )

        if result.returncode != 0:
            raise RuntimeError(
                f"ODA conversion failed (exit code {result.returncode}):\n"
                f"stdout: {result.stdout}\n"
                f"stderr: {result.stderr}"
            )

        # Find the output .dxf file
        dxf_filename = os.path.splitext(dwg_filename)[0] + ".dxf"
        dxf_path = os.path.join(output_dir, dxf_filename)

        if not os.path.exists(dxf_path):
            # Try case-insensitive search
            for f in os.listdir(output_dir):
                if f.lower().endswith(".dxf"):
                    dxf_path = os.path.join(output_dir, f)
                    break

        if not os.path.exists(dxf_path):
            raise RuntimeError(
                f"Conversion completed but no .dxf file found in output directory.\n"
                f"Output dir contents: {os.listdir(output_dir)}"
            )

        return dxf_path

    except subprocess.TimeoutExpired:
        raise RuntimeError("ODA conversion timed out after 120 seconds")
    finally:
        # Clean up input dir (output dir cleaned up by caller)
        shutil.rmtree(input_dir, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser(
        description="Convert .dwg to .dxf and extract spatial data"
    )
    parser.add_argument("input", help="Path to .dwg file")
    parser.add_argument("--output", "-o", help="Output JSON file path")
    parser.add_argument("--keep-dxf", action="store_true",
                        help="Keep the intermediate .dxf file")
    parser.add_argument("--dxf-output", help="Path to save the intermediate .dxf file")

    # Pass-through arguments for parse_dxf.py
    parser.add_argument("--layers", help="Layer filter (passed to parse_dxf.py)")
    parser.add_argument("--blocks-only", action="store_true")
    parser.add_argument("--hatches-only", action="store_true")
    parser.add_argument("--summary", action="store_true")
    parser.add_argument("--merge-with", help="Config JSON to merge into")

    args = parser.parse_args()

    # Validate input
    if not os.path.exists(args.input):
        print(f"ERROR: File not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    if not args.input.lower().endswith(".dwg"):
        print(f"ERROR: Expected .dwg file, got: {args.input}", file=sys.stderr)
        print("For .dxf files, use parse_dxf.py directly.", file=sys.stderr)
        sys.exit(1)

    # Check for ODA File Converter
    oda_binary = find_oda_converter()

    if not oda_binary:
        print("=" * 70, file=sys.stderr)
        print("ODA File Converter is NOT installed.", file=sys.stderr)
        print("", file=sys.stderr)
        print(".dwg files require the ODA File Converter for processing.", file=sys.stderr)
        print("", file=sys.stderr)
        print("RECOMMENDED WORKAROUND:", file=sys.stderr)
        print("Ask your architect to export .dxf alongside the PDF when", file=sys.stderr)
        print("issuing drawings. In AutoCAD this is one extra click in the", file=sys.stderr)
        print("publish routine.", file=sys.stderr)
        print("", file=sys.stderr)
        print("Suggested phrasing:", file=sys.stderr)
        print('  "Can you include DXF exports with the next drawing issue?', file=sys.stderr)
        print('   We\'re building digital project intelligence and the DXF', file=sys.stderr)
        print('   gives us exact geometry for quantity verification."', file=sys.stderr)
        print("", file=sys.stderr)
        print("ODA File Converter download (x86_64 Linux/Windows/Mac):", file=sys.stderr)
        print("  https://www.opendesign.com/guestfiles/oda_file_converter", file=sys.stderr)
        print("", file=sys.stderr)
        print("NOTE: ODA is currently only available for x86_64 systems.", file=sys.stderr)
        print("ARM64 (aarch64) is not supported.", file=sys.stderr)
        print("=" * 70, file=sys.stderr)
        sys.exit(1)

    # Convert .dwg → .dxf
    print(f"Converting {os.path.basename(args.input)} to DXF using ODA...", file=sys.stderr)
    output_dir = None

    try:
        dxf_path = convert_dwg_to_dxf(args.input, oda_binary)
        output_dir = os.path.dirname(dxf_path)
        print(f"Conversion successful: {dxf_path}", file=sys.stderr)

        # Save DXF if requested
        if args.keep_dxf or args.dxf_output:
            save_path = args.dxf_output or os.path.splitext(args.input)[0] + ".dxf"
            shutil.copy2(dxf_path, save_path)
            print(f"DXF saved to: {save_path}", file=sys.stderr)

        # Build parse_dxf.py command
        script_dir = os.path.dirname(os.path.abspath(__file__))
        parse_script = os.path.join(script_dir, "parse_dxf.py")

        cmd = [sys.executable, parse_script, dxf_path]

        if args.output:
            cmd.extend(["--output", args.output])
        if args.layers:
            cmd.extend(["--layers", args.layers])
        if args.blocks_only:
            cmd.append("--blocks-only")
        if args.hatches_only:
            cmd.append("--hatches-only")
        if args.summary:
            cmd.append("--summary")
        if args.merge_with:
            cmd.extend(["--merge-with", args.merge_with])

        # Run parse_dxf.py
        result = subprocess.run(cmd, capture_output=False)
        sys.exit(result.returncode)

    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        # Clean up temp output directory
        if output_dir and os.path.exists(output_dir):
            shutil.rmtree(output_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
