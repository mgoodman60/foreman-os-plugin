# Image Generation MCP Server — Setup Guide

This guide provides step-by-step instructions to install and configure the Foreman OS Image Generation MCP server.

## Prerequisites

Before starting, ensure you have:

- **Python 3.10 or higher** installed
  - Verify: `python3 --version`
  - Download from https://www.python.org/downloads/ if needed
- **pip** (Python package manager)
  - Verify: `pip --version`
  - Usually included with Python
- **Optional:** API keys from Flux 2 and/or Gemini (see "Getting API Keys" below)

## Step 1: Install Dependencies

Navigate to the `references/` directory and install required packages:

```bash
cd /path/to/image-generation-mcp/references
pip install -r requirements.txt
```

This installs:
- **mcp** — Anthropic's Model Context Protocol framework
- **httpx** — Async HTTP client for API requests
- **fastapi** — Web framework for the MCP server
- **uvicorn** — ASGI server to run the MCP server

### Troubleshooting Installation

**"Command not found: pip"**
- Use `pip3` instead: `pip3 install -r requirements.txt`

**"Permission denied"**
- Try: `pip install --user -r requirements.txt`
- Or use a Python virtual environment (recommended)

**Virtual Environment (Optional but Recommended)**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Step 2: Getting API Keys (Optional)

The server can function with just the SVG generator (no external APIs required). However, for Flux 2 and Gemini image generation, you'll need API keys.

### Option A: Flux 2 (Black Forest Labs)

Flux 2 generates photorealistic images and is ideal for high-quality renderings.

1. Visit https://api.bfl.ml/
2. Create an account or sign in
3. Navigate to API keys section
4. Generate a new API key
5. Copy the key — **keep it safe**
6. Set the environment variable (see Step 3)

**Cost:** Varies by tier; free tier available with rate limits

**Documentation:** https://docs.bfl.ml/

### Option B: Google Gemini

Gemini provides multimodal image generation with reference image support.

1. Visit https://aistudio.google.com/
2. Sign in with your Google account
3. Create an API key
4. Copy the key
5. Set the environment variable (see Step 3)

**Cost:** Free tier available; pay-as-you-go for higher usage

**Documentation:** https://ai.google.dev/

### Option C: Neither (SVG Only)

You can use the server with **only the SVG generator** and no API keys. The `generate_svg` tool will always be available, and the other tools will gracefully error if called.

## Step 3: Set Environment Variables

Environment variables tell the server which APIs are available.

### On macOS / Linux:

```bash
# Add these to your shell profile (~/.bash_profile, ~/.zshrc, etc.)
export FLUX2_API_KEY="your-flux2-api-key-here"
export GEMINI_API_KEY="your-gemini-api-key-here"

# Reload your shell
source ~/.bash_profile
```

Or set them per session:

```bash
export FLUX2_API_KEY="your-key"
export GEMINI_API_KEY="your-key"
python references/server.py
```

### On Windows (PowerShell):

```powershell
$env:FLUX2_API_KEY = "your-flux2-api-key-here"
$env:GEMINI_API_KEY = "your-gemini-api-key-here"
python references/server.py
```

### On Windows (Command Prompt):

```cmd
set FLUX2_API_KEY=your-flux2-api-key-here
set GEMINI_API_KEY=your-gemini-api-key-here
python references/server.py
```

### Verify Environment Variables Are Set:

```bash
echo $FLUX2_API_KEY
echo $GEMINI_API_KEY
```

Both should print your API keys. If they're empty or "not found", revisit the export command.

## Step 4: Run the Server

Start the MCP server:

```bash
python references/server.py
```

You should see output similar to:

```
======================================================================
Foreman OS Image Generation MCP Server
======================================================================
✓ Flux 2 API key detected - generate_image_flux2 available
✓ Gemini API key detected - generate_image_gemini available
✓ SVG generator always available - generate_svg ready

Available tools: generate_image_flux2, generate_image_gemini, generate_svg
Server ready to accept requests
======================================================================
```

The server will run on `http://localhost:3000` by default.

### Server Won't Start?

- **"Module not found"** — Re-run `pip install -r requirements.txt`
- **"Address already in use"** — Another service is using port 3000. Change the port in server.py
- **"API key not found"** — Verify environment variables with `echo $FLUX2_API_KEY`

## Step 5: Configure Claude / Foreman OS to Use the Server

Once the server is running, configure it within Claude or the Foreman OS plugin.

### For Claude Desktop:

1. Open Claude desktop settings
2. Navigate to "MCP Servers" or "Developer" settings
3. Add a new MCP server:
   - **Name:** foreman-image-gen
   - **Command:** `python`
   - **Arguments:** `/path/to/image-generation-mcp/references/server.py`
4. Restart Claude

### For Foreman OS Plugin:

The plugin should auto-detect the MCP server if it's running on the default port. If not:

1. Open plugin settings
2. Look for "MCP Server Configuration"
3. Add: `http://localhost:3000`
4. Restart the plugin

### Verify Tools Are Available:

Once configured, test that tools are accessible:

```bash
# In Claude or the plugin, try:
# @image-generation-mcp /generate_svg type="floor_plan" spatial_data={...}
```

You should see the SVG generator respond immediately. If Flux 2 or Gemini don't appear, verify their API keys are set.

## Step 6: Test the Tools

### Test SVG Generator (No API Key Required)

```bash
# This will always work
curl -X POST http://localhost:3000/tools/generate_svg \
  -H "Content-Type: application/json" \
  -d '{
    "type": "grid",
    "spatial_data": {"width": 200, "height": 300, "grid_spacing": 10},
    "options": {"show_dimensions": true}
  }'
```

You should receive SVG markup within ~100ms.

### Test Flux 2 (Requires FLUX2_API_KEY)

```bash
curl -X POST http://localhost:3000/tools/generate_image_flux2 \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "A modern healthcare facility surrounded by green landscaping",
    "width": 1024,
    "height": 768,
    "steps": 40
  }'
```

Expected wait time: 5-15 seconds. Response includes `image_base64`.

### Test Gemini (Requires GEMINI_API_KEY)

```bash
curl -X POST http://localhost:3000/tools/generate_image_gemini \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Construction site with heavy equipment and workers",
    "aspect_ratio": "16:9"
  }'
```

Expected wait time: 3-8 seconds. Response includes `image_base64`.

## Troubleshooting

### "FLUX2_API_KEY not set. Get an API key from https://api.bfl.ml/"

**Cause:** The environment variable isn't set or the server hasn't seen the update.

**Fix:**
1. Ensure the key is exported: `export FLUX2_API_KEY="..."`
2. Verify it's set: `echo $FLUX2_API_KEY`
3. **Restart the server** — it reads environment variables on startup
4. If still failing, check the server logs for more details

### Rate Limit Errors (429 responses)

**Cause:** Your API tier has a rate limit (common on free tier).

**Fix:**
- Flux 2: Upgrade tier at https://api.bfl.ml/
- Gemini: Check usage limits at https://aistudio.google.com/

The server implements exponential backoff and will retry automatically, but very aggressive usage may still hit limits.

### Generation Timeout (2 minutes for Flux 2)

**Cause:** Flux 2 is taking longer than the configured timeout (120 seconds).

**Fix:**
- For very detailed/large prompts, the timeout may be reached
- Reduce image dimensions (e.g., 512x512 instead of 1024x1024)
- Simplify the prompt
- If recurring, increase `FLUX2_TIMEOUT_SECONDS` in `server.py` (line ~50)

### SVG Generation Produces Invalid Markup

**Cause:** `spatial_data` structure doesn't match expected schema.

**Fix:**
- For floor plans: ensure `spatial_data` has `rooms` array with `{name, x, y, width, height, type}`
- For site plans: ensure `spatial_data` has `building`, `parking`, `drives`, `utilities` objects
- See examples in SKILL.md or the tool documentation

### Gemini Content Safety Filter Blocks Image

**Cause:** Gemini's content filter rejected the prompt.

**Fix:**
- Rephrase the prompt to avoid triggering filters
- Example: Instead of "dangerous construction site", try "busy construction site with active crews"
- If the issue persists, the prompt may violate usage policies

### Port 3000 Already in Use

**Cause:** Another service is listening on port 3000.

**Fix:**
- Find what's using it: `lsof -i :3000` (macOS/Linux)
- Kill it or modify the server to use a different port
- In `server.py`, change the port in the uvicorn config (end of file)

## Advanced Configuration

### Custom Timeout Settings

Edit `references/server.py` (around line 50):

```python
FLUX2_TIMEOUT_SECONDS = 120  # Change to 180 for 3 minutes
HTTPX_TIMEOUT = 30  # HTTP request timeout
POLL_INTERVAL = 2  # Seconds between Flux 2 polling
```

### Logging Level

Change logging verbosity in `server.py`:

```python
logging.basicConfig(
    level=logging.DEBUG,  # Change to DEBUG for more details
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Running as a Background Service (macOS/Linux)

Create a systemd service file or LaunchAgent:

**systemd (Linux):**
```ini
[Unit]
Description=Foreman Image Generation MCP Server
After=network.target

[Service]
Type=simple
User=your-user
ExecStart=/usr/bin/python3 /path/to/server.py
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Enable with: `systemctl enable foreman-image-gen`

## Next Steps

1. **Test in Your Plugin:** Once the server is configured, use the `/render` command in Foreman OS to generate images
2. **Check Logs:** Monitor the server output for any errors or warnings
3. **Optimize Settings:** Adjust timeouts and scales based on your typical usage
4. **Monitor Costs:** If using paid API tiers, watch your usage on the provider dashboards

## Support

- **Flux 2 Issues:** https://docs.bfl.ml/ or support@bfl.ml
- **Gemini Issues:** https://support.google.com/ai-studio/
- **MCP Protocol:** https://modelcontextprotocol.io/
- **Foreman OS Issues:** Check the main Foreman OS documentation

## Quick Command Reference

| Task | Command |
|------|---------|
| Install | `pip install -r requirements.txt` |
| Set Flux 2 Key | `export FLUX2_API_KEY="key"` |
| Set Gemini Key | `export GEMINI_API_KEY="key"` |
| Run Server | `python references/server.py` |
| Check Keys | `echo $FLUX2_API_KEY` |
| Test SVG | `curl http://localhost:3000/tools` |
| Stop Server | `Ctrl+C` in terminal |
