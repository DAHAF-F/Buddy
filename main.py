"""
Buddy — Unified Entry Point
============================
A convenience launcher for both components of the Buddy AI assistant.

Usage:
    python main.py server          # Start the MCP server (port 8000)
    python main.py agent           # Start the LiveKit voice agent (dev mode)
    python main.py agent dev       # Explicit dev mode
    python main.py agent console   # Console / text-only mode

For production use, prefer the uv scripts defined in pyproject.toml:
    uv run buddy          → MCP server
    uv run buddy_voice    → Voice agent (dev mode)
"""

import sys


def main():
    args = sys.argv[1:]

    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)

    command = args[0].lower()

    if command == "server":
        # Start the MCP / FastMCP server
        from server import main as server_main
        server_main()

    elif command == "agent":
        # Pass remaining args (e.g. "dev", "console") to agent_buddy
        remaining = args[1:]
        if remaining:
            sys.argv = [sys.argv[0]] + remaining
        else:
            # Default to dev mode so the voice agent auto-starts
            sys.argv = [sys.argv[0], "dev"]
        from agent_buddy import main as agent_main
        agent_main()

    else:
        print(f"Unknown command: {command!r}")
        print("Use 'server' or 'agent'. Run with --help for details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
