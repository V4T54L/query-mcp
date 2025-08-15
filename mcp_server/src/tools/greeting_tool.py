# This module contains a specific tool. By separating tools into different
# files, we keep the codebase organized and easy to navigate.

import logging
from typing import Optional

# Note that this file does not depend on the server implementation (FastMCP).
# The function is a standard async Python function, making it highly portable
# and easy to test in isolation.

async def greet_user(name: str, title: Optional[str] = None) -> str:
    """
    Generates a friendly greeting for a user.

    This tool is useful for creating personalized welcome messages. The docstring
    is critical as it's used by the LLM to understand how to use the tool.

    Args:
        name: The first name of the person to greet.
        title: An optional title for the person (e.g., 'Dr.', 'Mx.').

    Returns:
        A string containing the formatted greeting message.
    """
    try:
        logging.info(f"Executing greet_user tool for name='{name}' and title='{title}'")
        if title:
            greeting = f"Hello, {title} {name}! Welcome to the MCP server."
        else:
            greeting = f"Hello, {name}! Welcome to the MCP server."
        return greeting
    except Exception as e:
        logging.error(f"An error occurred in greet_user: {e}")
        return "Sorry, I was unable to generate a greeting."
