import json


def get_user_input():
    command = input("📥 Enter command (e.g., 'check engine health'): ")

    telemetry_raw = input(
        "📊 Enter fake telemetry (JSON) or leave empty: ").strip()
    telemetry = {}

    if telemetry_raw:
        try:
            telemetry = json.loads(telemetry_raw)
        except json.JSONDecodeError:
            print("⚠️ Invalid JSON. Proceeding with empty telemetry.")

    return command, telemetry


def what_next(tel):
    if tel:
        return print(tel)
    else:
        print("nothing...")
