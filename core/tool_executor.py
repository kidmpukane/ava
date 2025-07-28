# core/tool_executor.py

from tools.registry import diagnose_engine, check_temperature, oil_pressure_alert

TOOL_LIST = {
    "EngineDiagnosticTool": diagnose_engine,
    "TemperatureCheckTool": check_temperature,
    "OilPressureMonitor": oil_pressure_alert,
}


def tool_executor(suggested_tool, **kwargs):
    tool = TOOL_LIST.get(suggested_tool)
    if tool:
        try:
            result = tool(**kwargs)
            return {
                "success": True,
                "tool": suggested_tool,
                "output": result
            }
        except Exception as e:
            return {
                "success": False,
                "tool": suggested_tool,
                "error": f"Error running tool: {e}"
            }
    else:
        return {
            "success": False,
            "tool": suggested_tool,
            "error": f"Tool '{suggested_tool}' is not recognized or available."
        }
