import asyncio
from fastmcp import Client

async def main():
    # Connect to the running server over HTTP
    client = Client("http://localhost:8000/mcp")

    # The client will communicate with the already running mcp server via HTTP
    async with client:
        # Call the MCP tool named "hello", arguments must match the tool's schema
        result = await client.call_tool("hello", {"name": "world"})

        # Print the tool's return value
        print(result)

# Required because MCP client APIs are async
asyncio.run(main())