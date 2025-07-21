# ava/tools/registry.py

def echo_tool(message):
    return f"You said: {message}"

TOOL_REGISTRY = {
    "echo": echo_tool
}
