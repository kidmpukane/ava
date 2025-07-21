# ava/core/tool_executor.py

def execute_tool(tool_fn, params):
    return tool_fn(**params)
