# MCP Basic Examples

<img width="85" alt="map-user" src="https://img.shields.io/badge/views-021-green"> <img width="125" alt="map-user" src="https://img.shields.io/badge/unique visits-000-green">

Simple examples to help you get started understanding MCP and tool calling on your local host.

Your MCP server supports communication to a client via. either standard input / output (stdio) or HTTP.

Standard input / output (stdio) works well when your MCP server does NOT need to be reused by multiple clients. Using stdio the client starts and runs the MCP server as a subprocess.

HTTP is a better option when you are building an MCP server where reusability from multiple clients is a requirement. With HTTP you can run the server independently and multiple clients can connect as needed.

## Standard Input / Output (stdio) Example

The [STDIO folder](https://github.com/ev2900/MCP_Basics/tree/main/STDIO) has the required artifacts to run an MCP server with a simple hello world tool.

Begin by installing the required python libraries

```
pip install -r requirements.txt
```

Then run the client

```
python client.py
```

The client starts a sub-process that runs the MCP server. The response from the MCP server is printed to the console.

## HTTP Example

The [HTTP folder](https://github.com/ev2900/MCP_Basics/tree/main/HTTP) has the required artifacts to run an MCP server with a simple hello world tool.

Begin by installing the required python libraries

```
pip install -r requirements.txt
```

Then start the MCP server

```
python server.py
```

Once the MCP server is running, run the client

```
python client.py
```

The response from the "remote" MCP server is printed to the console.
