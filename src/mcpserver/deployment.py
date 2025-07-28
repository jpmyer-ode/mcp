# server py file for MCP
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

#add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two integers."""
    return a + b