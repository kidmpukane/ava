# ava/core/tool_selector.py

from tools.registry import TOOL_REGISTRY


def select_tool(intent, params):
    return TOOL_REGISTRY.get(intent)
