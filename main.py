from core.input_handler import get_user_input
from core.intent_analyser import intent_analyser
from core.tool_selector import select_tool
from core.tool_executor import execute_tool
from utils.startup import palantir_boot
import time


def main():
    palantir_boot()

    defined_input = get_user_input()

    print("  Processing Input...")
    time.sleep(0.25)

    # --- Step 1: Intent Analysis ---
    user_intent = intent_analyser(
        defined_input["command"],
        defined_input["machine_id"],
        defined_input["sensor"],
        defined_input["window"]
    )

    print("\n  ┌─ Intent Analysis")
    print("  │")
    print(f"  │  Intent:       {user_intent['intent']}")
    print(f"  │  Confidence Score:       {user_intent['score']}")
    print(f"  │  Machine ID:   {user_intent['machine_id']}")
    print(f"  │  Sensor:       {user_intent['params']['sensor']}")
    print(f"  │  Window:       {user_intent['params']['window']}")
    print("  └───────────────────────────────\n")
    time.sleep(0.4)

    # --- Step 2: Tool Selection ---
    selected_tool_payload = select_tool(user_intent)

    print("  ┌─ Tool Selection")
    print("  │")
    print(f"  │  Selected Tool: {selected_tool_payload['tool']}")
    print("  └───────────────────────────────\n")
    time.sleep(0.4)

    # --- Step 3: Tool Execution ---
    result = execute_tool(selected_tool_payload)

    print("  ┌─ Execution Result")
    print("  │")
    print(f"  │  Status:  {result['status']}")
    print(f"  │  Output:  {result['output']}")
    print(f"  │  Using:   {result['metadata']['tool']}")
    print("  └───────────────────────────────\n")


if __name__ == "__main__":
    main()


# {"intent": "check_temperature",
# "confidence": 0.87,
# "machine_id": 12,
# "parameters":
#       {"sensor": "Sensor_4",
#        "window": 12}, "raw_input": "
#               Check Sensor_4 temperature for machine 12 over last 12 hours"}
