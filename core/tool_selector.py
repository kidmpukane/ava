from tools.registry import tool_dict
TOOL_MAP = {
    "diagnose_engine": "EngineDiagnosticTool",
    "check_temperature": "TemperatureCheckTool",
    "oil_pressure_alert": "OilPressureMonitor",
}

ALLOWED_INTENTS = {
    "diagnose_engine": "EngineDiagnosticTool",
    "check_temperature": "TemperatureCheckTool",
    "oil_pressure_alert": "OilPressureMonitor",
}


def is_allowed(intent):
    return intent in ALLOWED_INTENTS


def get_tool_name(intent):
    return ALLOWED_INTENTS.get(intent, None)


def select_tool(user_intent):
    intent = user_intent["intent"]
    if not is_allowed(intent):
        return (f"❌ Intent '{intent}' is not allowed.")
    else:
        None
    tool_name = get_tool_name(intent)

    return {
        "tool": tool_name,
        "intent": intent,
        "machine_id": user_intent["machine_id"],
        "params": {
            "sensor": user_intent["params"]["sensor"],
            "window": user_intent["params"]["window"]
        }
    }
