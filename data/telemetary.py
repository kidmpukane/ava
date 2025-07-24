import time
import json
import random
import threading
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta


@dataclass
class Telemetary_Data:
    machine_id: str
    battery_level: float
    temperature: float
    vibration: float
    timestamp: str

    def to_json(self):
        return json.dumps(asdict(self), indent=2)


def generate_random_telemetry(forklift_number=None):
    """Generate random telemetry data for a forklift"""

    # Generate random forklift number if not provided
    if forklift_number is None:
        forklift_number = random.randint(1, 999)

    # Format machine ID
    machine_id = f"forklift-{forklift_number:03d}"

    # Generate realistic random values
    battery_level = round(random.uniform(15.0, 100.0), 1)  # 15% to 100%
    temperature = round(random.uniform(20.0, 65.0), 1)  # 20°C to 65°C
    vibration = round(random.uniform(0.1, 2.0), 2)  # 0.1 to 2.0 units

    # Generate timestamp (current time with some random offset)
    base_time = datetime.now()
    random_offset = timedelta(minutes=random.randint(-60, 60))
    timestamp = (base_time + random_offset).isoformat() + "Z"

    return Telemetary_Data(
        machine_id=machine_id,
        battery_level=battery_level,
        temperature=temperature,
        vibration=vibration,
        timestamp=timestamp
    )


def json_conv():
    telemetry = generate_random_telemetry()
    print(telemetry.to_json())


def timer_function(x):
    i = 10
    while i > 0:
        time.sleep(5)
        x()
        i -= 1
    else:
        return "Process Finished"


# Generate single random telemetry
print("Single random telemetry:")
timer_function(json_conv)
