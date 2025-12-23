import asyncio
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

async def main():
	# Create an MCP client that will START the server as a subprocess using: `python server.py`
    client = Client(StdioTransport(command="python", args=["server.py"]))

    # The client will communicate with that subprocess mcp server via stdin/stdout
    async with client:
    	# Call the MCP tool named "hello", arguments must match the tool's schema
        result = await client.call_tool("hello", {"name": "world"})
        
        # Print the tool's return value
        print(result)

# Required because MCP client APIs are async
asyncio.run(main())