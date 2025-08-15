# This module is responsible for setting up and running the MCP server.
# It handles server configuration, tool registration, and startup.

import logging
from mcp.server.fastmcp import FastMCP

# Import the specific tool functions that need to be registered.
# This approach is explicit and avoids magic. For a very large number of tools,
# you could implement an auto-discovery mechanism that imports all tools
# from the 'tools' directory.
from src.tools.greeting_tool import greet_user

def setup_logging():
    """Configures the application's logging for better monitoring."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def create_server() -> FastMCP:
    """
    Creates and configures the FastMCP server instance and registers tools.
    
    Returns:
        An instance of FastMCP with all tools registered.
    """
    logging.info("Initializing MCP server...")
    # The server name can be loaded from a configuration file in a real app.
    mcp_server = FastMCP("ProductionGradeServer")

    # --- Tool Registration ---
    # Instead of using the @mcp.tool() decorator on the function itself,
    # we explicitly register the imported functions with the server instance.
    # This decouples the tool's code from the server's implementation.
    logging.info("Registering tools...")
    mcp_server.tool(greet_user)
    # Example: If you had another tool, you would register it here:
    # from src.tools.status_tool import get_server_status
    # mcp_server.tool(get_server_status)

    logging.info("Tool registration complete.")
    return mcp_server

def main():
    """
    The main function to set up logging, create, and run the server.
    """
    setup_logging()
    server = create_server()
    
    logging.info("Starting MCP server...")
    # The transport protocol can be configured via environment variables
    # or a config file for a true production setup. 'stdio' is used here
    # for local development and compatibility with clients like VS Code.
    server.run(transport='stdio')
    logging.info("MCP server has stopped.")
