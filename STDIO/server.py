from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("STDIO-mcp")

# Define a tool
@mcp.tool()
def hello(name: str) -> str:
    """
    Say hello to someone
    """
    return f"Hello, {name}!"

# Run the server
if __name__ == "__main__":
    mcp.run()