import json
from datetime import datetime, timedelta
import random

import random
from datetime import datetime, timedelta
import json


def apple_watch_mock_wearable_data(num_users=4, num_records_per_user=5):
    apple_watch_data = []
    for i in range(1, num_users + 1):
        for _ in range(num_records_per_user):
            record = {
                "user_id": f"P{i:03d}",
                "timestamp": (
                    datetime.now() - timedelta(hours=random.randint(1, 24))
                ).isoformat()
                + "Z",
                "heart_rate_bpm": random.randint(70, 100),  # Mildly elevated
                "hrv_ms": random.randint(20, 60),  # Lower HRV
                "sleep_stage": random.choice(
                    ["awake", "light", "light", "REM"]
                ),  # Disrupted sleep
                "steps_count": random.randint(1000, 5000),  # Reduced activity
            }
            apple_watch_data.append(record)

    # Save to JSON file
    with open("mock_data/apple_watch_data.json", "w") as f:
        json.dump(apple_watch_data, f, indent=4)


def fitbit_mock_wearable_data(num_users=4, num_records_per_user=5):
    fitbit_data = []
    for i in range(1, num_users + 1):
        for _ in range(num_records_per_user):
            record = {
                "user_id": f"P{i:03d}",
                "timestamp": (
                    datetime.now() - timedelta(hours=random.randint(1, 24))
                ).isoformat()
                + "Z",
                "heartRate": random.randint(70, 100),  # Mildly elevated
                "hrv": random.randint(20, 60),  # Lower HRV
                "sleep": random.choice(
                    ["awake", "light", "light", "REM"]
                ),  # Disrupted sleep
                "steps": random.randint(1000, 5000),  # Reduced activity
            }
            fitbit_data.append(record)
    with open("mock_data/fitbit_data.json", "w") as f:
        json.dump(fitbit_data, f, indent=4)


def garmin_mock_wearable_data(num_users=4, num_records_per_user=5):
    garmin_data = []
    for i in range(1, num_users + 1):
        for _ in range(num_records_per_user):
            record = {
                "user_id": f"P{i:03d}",
                "timestamp": (
                    datetime.now() - timedelta(hours=random.randint(1, 24))
                ).isoformat()
                + "Z",
                "bpm": random.randint(70, 100),  # Mildly elevated
                "hrv": random.randint(20, 60),  # Lower HRV
                "sleep_score": random.choice([60, 80, 90]),  # Simulate sleep scores
                "steps": random.randint(1000, 5000),  # Reduced activity
            }
            garmin_data.append(record)
    with open("mock_data/garmin_data.json", "w") as f:
        json.dump(garmin_data, f, indent=4)

    print("Mock wearable data generated and saved to JSON files.")


if __name__ == "__main__":
    apple_watch_mock_wearable_data()
    fitbit_mock_wearable_data()
    garmin_mock_wearable_data()
