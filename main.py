# main.py

from core.input_handler import get_user_input
from core.intent_analyser import analyse_intent
from core.tool_selector import select_tool
from core.tool_executor import tool_executor


def main():
    print("🚀 AVA is online.")

    command, telemetry = get_user_input()
    intent = analyse_intent(command)
    selected_tool = select_tool(intent)

    # Build args based on tool
    if selected_tool == "EngineDiagnosticTool":
        result = tool_executor(
            selected_tool,
            temp=telemetry.get("temp", 0),
            vib=telemetry.get("vib", 0),
            oil=telemetry.get("oil", 0)
        )
    else:
        result = tool_executor(selected_tool, sensor_data=telemetry)

    # Output result
    print("\n✅ Success" if result["success"] else "❌ Failure")
    print(f"🔎 Intent: {intent}")
    print(f"🔧 Tool: {selected_tool}")
    print(f"📤 Output: {result.get('output') or result.get('error')}")


if __name__ == "__main__":
    main()


# {"temp": 95, "vib": 0.6, "oil": 28}
