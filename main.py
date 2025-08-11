from core.input_handler import get_user_input
from core.intent_analyser import intent_analyser


def main():
    defined_input = get_user_input()
    user_intent = intent_analyser(
        defined_input["command"],
        defined_input["machine_id"],
        defined_input["sensor"],
        defined_input["window"]
    )
    return print(user_intent)


if __name__ == "__main__":
    main()


# {"intent": "check_temperature", "confidence": 0.87, "machine_id": 12, "parameters": {"sensor": "Sensor_4", "window": 12}, "raw_input": "Check Sensor_4 temperature for machine 12 over last 12 hours"}
