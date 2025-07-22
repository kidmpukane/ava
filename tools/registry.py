# ava/tools/registry.py

def diagnose_engine():
    checklist = [
        "Checking engine temperature...",
        "Checking oil pressure levels...",
        "Scanning for error codes...",
        "Listening for unusual engine noises...",
        "Inspecting spark plugs and ignition...",
        "Verifying fuel injection system...",
        "Analyzing exhaust emissions..."
    ]

    for task in checklist:
        print(task)


def check_temperature():
    print("✅ Engine temperature is within safe operating range.")


def oil_pressure_alert():
    print("⚠️ Oil pressure is slightly below optimal. Recommend inspection.")


def tool_dict():
    custom_tool = "No current available tool matches found."
    return custom_tool
