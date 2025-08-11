from core.intent_classifier import IntentClassifier

# Initialize once (can preload from a config or intent JSON)
intent_examples = {
    "diagnose_engine": ["check engine", "engine fault", "engine error"],
    "check_temperature": ["temperature", "heat", "overheating"],
    "oil_pressure_alert": ["oil pressure", "low oil", "check oil"],
    "get_historical_data": [
        "Show past logs",
        "I want historical data",
        "Pull previous records",
    ],
}


def intent_analyser(user_intent, machine_id, sensor, window):
    classifier = IntentClassifier(intent_examples)  # pass the examples
    predicted_label, score = classifier.predict(user_intent)  # unpack tuple
    intent_specs = {
        "intent": predicted_label,
        "score": score,
        "machine_id": machine_id,
        "params": {
            "sensor": sensor,
            "window": window
        }
    }
    return intent_specs
