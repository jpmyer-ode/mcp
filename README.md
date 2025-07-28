# Installation Steps

To install the 'add_tool' MCP server, run the following mcp command:

'''json
{
  "mcpServers": {
  "add_tool": {
	"command": "C:\\Users\\jmyer\\.local\\bin\\uvx.EXE",
    "args": [
      "--from",
      "git+https://github.com/jpmyer-ode/mcp.git",
      "mcp-server"
    ]
  }
}
'''

This will fetch and setup the 'mcp-server' from the specified GitHub repository