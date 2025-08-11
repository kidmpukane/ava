import json
from datetime import datetime


def get_user_input():
    command = input("📥 Enter command (e.g., 'check engine health'): ")
    machine_id = (input("What is the Machine ID In Question?: "))
    sensor = input(
        f"What is the Sesnsor incharge of Machine ID: {machine_id}?: ")
    now = datetime.now()
    window = now.strftime("%H:%M:%S")

    req_structure = {
        "command": command,
        "machine_id": int(machine_id),
        "sensor": (f"Sensor_{int(sensor)}"),
        "window": window,
    }

    return req_structure
