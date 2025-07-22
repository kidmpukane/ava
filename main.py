from core.input_handler import get_user_input
from core.intent_analyser import analyse_intent
from core.tool_selector import select_tool


def main():
    print("🚀 AVA is online.")
    user_input = get_user_input()
    intent = analyse_intent(user_input)
    tool = select_tool(intent)

    print(f"\n🔎 Identified Intent: {intent}")
    print(f"🔧 Suggested Tool: {tool}")


if __name__ == "__main__":
    main()
