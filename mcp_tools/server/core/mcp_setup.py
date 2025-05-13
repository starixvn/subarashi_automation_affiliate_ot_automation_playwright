import os
import nest_asyncio
from mcp.server.fastmcp import FastMCP
from mcp_tools.server.core.manager import PlaywrightManager

# Apply nest_asyncio to allow nested asyncio event loops
nest_asyncio.apply()

# Create FastMCP instance
mcp = FastMCP(
    name="PlaywrightAutomation", dependencies=["playwright", "nest_asyncio", "psutil"]
)

# Create PlaywrightManager instance
pw_manager = PlaywrightManager(
    browser_type="chromium", headless=False, viewport_port=(1200, 900)
)

# Set work directory
work_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import mcp_tools.server.browser
import mcp_tools.server.content
import mcp_tools.server.api
import mcp_tools.server.database
import mcp_tools.server.google
