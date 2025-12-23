from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("HTTP-mcp")

# Define a tool
@mcp.tool
def hello(name: str) -> str:
    """
    Say hello to someone
    """
    return f"Hello, {name}!"

# Run the server
if __name__ == "__main__":
    # MCP endpoint will be: http://localhost:8000/mcp
    mcp.run(transport="http", host="127.0.0.1", port=8000)