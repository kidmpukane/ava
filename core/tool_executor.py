from tools.registry import diagnose_engine, check_temperature, oil_pressure_alert

TOOL_LIST = {
    "EngineDiagnosticTool": diagnose_engine,
    "TemperatureCheckTool": check_temperature,
    "OilPressureMonitor": oil_pressure_alert,
}


def execute_tool(retrive_tool):
    if type(retrive_tool) == dict:
        tool_name = retrive_tool["tool"]
        if tool_name:
            tool_fn = TOOL_LIST.get(tool_name)
            if not tool_fn:
                print(f"⚠️ Tool '{tool_name}' not found in registry.")
                return None

            result = tool_fn()
            return {
                "status": "success",
                "output": result,
                "metadata": retrive_tool,
            }
        else:
            print("Error occured during the execution phase...")
    else:
        return ("Error occured in intent layer... Your intentions could not be processed")
