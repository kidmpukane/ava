INTENT_KEYWORDS = {
    "diagnose_engine": ["check engine", "engine fault", "engine error"],
    "check_temperature": ["temperature", "heat", "overheating"],
    "oil_pressure_alert": ["oil pressure", "low oil", "check oil"],
}


def analyse_intent(user_input):
    for intent, keywords in INTENT_KEYWORDS.items():
        if any(keyword in user_input.lower() for keyword in keywords):
            return intent
    return "unknown_intent"
