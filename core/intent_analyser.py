from core.intent_classifier import IntentClassifier

# Initialize once (can preload from a config or intent JSON)
intent_examples = {
    "diagnose_engine": ["check engine", "engine fault", "engine error"],
    "check_temperature": ["temperature", "heat", "overheating"],
    "oil_pressure_alert": ["oil pressure", "low oil", "check oil"],
}
intent_classifier = IntentClassifier(intent_examples)

# In your input handler / reasoning flow
user_input = "Please show logs from yesterday"
intent, score = intent_classifier.predict(user_input)

if intent:
    tool = ToolSelector.pick_tool(intent)
    response = ToolExecutor.run(tool, user_input)
else:
    response = OutputHandler.ask_for_clarification(user_input)
