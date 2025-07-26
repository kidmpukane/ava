from tools.registry import diagnose_engine, check_temperature, oil_pressure_alert

TOOL_LIST = {
    "EngineDiagnosticTool": diagnose_engine,
    "TemperatureCheckTool": check_temperature,
    "OilPressureMonitor": oil_pressure_alert,
}


def tool_executor(suggested_tool):
    tool = TOOL_LIST.get(suggested_tool)
    if tool:
        tool()
    else:
        raise ValueError(
            f"Tool '{suggested_tool}' is not recognized or available.")
