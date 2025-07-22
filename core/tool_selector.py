from tools.registry import tool_dict
TOOL_MAP = {
    "diagnose_engine": "EngineDiagnosticTool",
    "check_temperature": "TemperatureCheckTool",
    "oil_pressure_alert": "OilPressureMonitor",
}


def select_tool(intent):
    return TOOL_MAP.get(intent, tool_dict())
