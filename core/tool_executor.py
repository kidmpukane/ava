from tools.registry import diagnose_engine, check_temperature, oil_pressure_alert

suggested_tools = {
    "EngineDiagnosticTool": diagnose_engine,
    "TemperatureCheckTool": check_temperature,
    "OilPressureMonitor": oil_pressure_alert,
}


def tool_executor(tool, suggested_tool):
    # Take selected_tool as input

    # Execute tool
    # Report
    pass
