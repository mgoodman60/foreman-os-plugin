#!/bin/bash
# compile_libredwg.sh — Build dwg2dxf from libredwg source
#
# This script compiles the libredwg library and dwg2dxf converter from source.
# It uses direct gcc compilation (no cmake/autotools required) with a manually
# crafted config.h that handles all platform-specific defines.
#
# The binary is cached at /tmp/libredwg/dwg2dxf and reused across invocations
# within the same session.
#
# Usage: bash compile_libredwg.sh
# Output: /tmp/libredwg/dwg2dxf binary

set -e

INSTALL_DIR="/tmp/libredwg"
BINARY="$INSTALL_DIR/dwg2dxf"

# Check for cached binary
if [ -f "$BINARY" ]; then
    echo "dwg2dxf binary already exists at $BINARY"
    echo "Skipping compilation."
    exit 0
fi

echo "=== Compiling libredwg from source ==="

# Clean slate
rm -rf "$INSTALL_DIR"

# Clone repository (shallow for speed)
echo "Cloning libredwg repository..."
cd /tmp
git clone --depth 1 https://github.com/LibreDWG/libredwg.git
cd libredwg

# Create config.h
# This config was developed through trial-and-error to work without
# autotools/cmake. It defines the minimum set of platform features
# needed for DWG→DXF conversion on Linux.
echo "Creating config.h..."
cat > src/config.h << 'CONFIGEOF'
#define PACKAGE "libredwg"
#define PACKAGE_VERSION "0.13"
#define PACKAGE_STRING "libredwg 0.13"
#define LIBREDWG_SO_VERSION "0:13:0"
#define HAVE_STDINT_H 1
#define HAVE_STDLIB_H 1
#define HAVE_STRING_H 1
#define HAVE_STRINGS_H 1
#define HAVE_INTTYPES_H 1
#define HAVE_UNISTD_H 1
#define HAVE_CTYPE_H 1
#define HAVE_WCHAR_H 1
#define HAVE_WCTYPE_H 1
#define HAVE_MEMCHR 1
#define HAVE_MEMMEM 1
#define HAVE_SCANDIR 1
#define IS_RELEASE 1
#define PACKAGE_NAME "libredwg"
#define HAVE_SYS_STAT_H 1
CONFIGEOF

# Compile library object files
# Skip in_json.c (needs jsmn.h submodule) and out_geojson.c (extra errors)
# Neither is needed for DWG→DXF conversion
echo "Compiling library sources..."
gcc -c -I. -Iinclude -Isrc -DHAVE_CONFIG_H \
  src/bits.c src/common.c src/classes.c src/codepages.c \
  src/decode.c src/decode_r11.c src/decode_r2007.c \
  src/dwg.c src/dwg_api.c src/hash.c src/dynapi.c \
  src/dxfclasses.c src/out_dxf.c src/out_json.c \
  src/print.c src/free.c src/encode.c -w

# Compile dwg2dxf program
echo "Compiling dwg2dxf..."
gcc -c -I. -Iinclude -Isrc -DHAVE_CONFIG_H programs/dwg2dxf.c -w

# Link
echo "Linking..."
gcc -o dwg2dxf *.o -lm -w

# Verify
if [ -f "$BINARY" ]; then
    echo ""
    echo "=== Compilation successful ==="
    echo "Binary: $BINARY"
    ls -la "$BINARY"
else
    echo ""
    echo "=== Compilation FAILED ==="
    echo "The dwg2dxf binary was not produced."
    exit 1
fi
