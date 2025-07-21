# ava/main.py

from core.input_handler import get_input
from core.intent_analyser import analyse_intent
from core.tool_selector import select_tool
from core.tool_executor import execute_tool
from core.response_generator import generate_response
from core.output_handler import output_result


def main():
    print("🚀 AVA is online. Awaiting input...\n")

    # Step 1: Get input (sensor data, user prompt, etc.)
    input_data = get_input()

    # Step 2: Analyze intent
    intent, params = analyse_intent(input_data)

    # Step 3: Select tool + validate
    tool = select_tool(intent, params)

    if not tool:
        print("⚠️ AVA could not find a valid tool for this intent.")
        return

    # Step 4: Execute tool
    result = execute_tool(tool, params)

    # Step 5: Generate output
    response = generate_response(result)

    # Step 6: Display or output response
    output_result(response)


if __name__ == "__main__":
    main()
