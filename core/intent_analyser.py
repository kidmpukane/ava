from core.intent_classifier import IntentClassifier

# --- Initialize once (global, fast, stable) ---
intent_examples = {
    "diagnose_engine": ["check engine", "engine fault", "engine error"],
    "check_temperature": ["temperature", "heat", "overheating"],
    "oil_pressure_alert": ["oil pressure", "low oil", "check oil"],
    "get_historical_data": [
        "show past logs",
        "i want historical data",
        "pull previous records",
    ],
}

classifier = IntentClassifier(intent_examples)  # <-- persistent instance


def intent_analyser(user_intent, machine_id, sensor, window):

    # --- Predict intent (returns: label, confidence_score) ---
    predicted_label, score = classifier.predict(user_intent)

    # --- Unified Output Schema ---
    return {
        "intent": predicted_label,
        "score": score,
        "machine_id": machine_id,
        "params": {
            "sensor": sensor,
            "window": window,
        },
    }
