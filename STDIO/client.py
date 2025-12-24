import asyncio
from fastmcp import Client
from fastmcp.client.transports import StdioTransport

async def main():
	# Create an MCP client that will START the server as a subprocess using: `python server.py`
    client = Client(StdioTransport(command="python", args=["server.py"]))

    # The client will communicate with the already running mcp server via HTTP
    async with client:
        # Get a list of all the tools available via. the MCP server
        result_1 = await client.list_tools()

        # Print the name and description of each tool
        print('-- Tools --')
        for tool in result_1:
            # print(tool)
            print(f'Name: {tool.name}')
            print(f'Description: {tool.description}')

        # Call the MCP tool named "hello", arguments must match the tool's schema
        result_2 = await client.call_tool("hello", {"name": "world"})

        # Print the tool's return value
        print('-- Result from calling hello tool --')
        # print(result_2)
        print(result_2.content[0].text)

# Required because MCP client APIs are async
asyncio.run(main())
