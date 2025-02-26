import json
from datetime import datetime, timedelta
import random


def generate_mock_wearable_data(num_users=100, num_records_per_user=5):
    # Device 1: Apple Watch
    apple_watch_data = []
    for i in range(1, num_users + 1):
        for _ in range(num_records_per_user):
            record = {
                "user_id": f"U{i:03d}",
                "timestamp": (
                    datetime.now() - timedelta(hours=random.randint(1, 24))
                ).isoformat()
                + "Z",
                "heart_rate_bpm": random.randint(60, 100),
                "hrv_ms": random.randint(20, 100),
                "sleep_stage": random.choice(["light", "deep", "REM"]),
                "steps_count": random.randint(0, 10000),
            }
            apple_watch_data.append(record)

    # Device 2: Fitbit
    fitbit_data = []
    for i in range(1, num_users + 1):
        for _ in range(num_records_per_user):
            record = {
                "user_id": f"U{i:03d}",
                "timestamp": (
                    datetime.now() - timedelta(hours=random.randint(1, 24))
                ).isoformat()
                + "Z",
                "heartRate": random.randint(60, 100),
                "hrv": random.randint(20, 100),
                "sleep": random.choice(["light", "deep", "REM"]),
                "steps": random.randint(0, 10000),
            }
            fitbit_data.append(record)

    # Device 3: Garmin
    garmin_data = []
    for i in range(1, num_users + 1):
        for _ in range(num_records_per_user):
            record = {
                "user_id": f"U{i:03d}",
                "timestamp": (
                    datetime.now() - timedelta(hours=random.randint(1, 24))
                ).isoformat()
                + "Z",
                "bpm": random.randint(60, 100),
                "hrv": random.randint(20, 100),
                "sleep_score": random.choice([60, 80, 90]),  # Simulate sleep scores
                "steps_taken": random.randint(0, 10000),
            }
            garmin_data.append(record)

    # Save to JSON files
    with open("apple_watch_data.json", "w") as f:
        json.dump(apple_watch_data, f, indent=4)
    with open("fitbit_data.json", "w") as f:
        json.dump(fitbit_data, f, indent=4)
    with open("garmin_data.json", "w") as f:
        json.dump(garmin_data, f, indent=4)

    print("Mock wearable data generated and saved to JSON files.")


if __name__ == "__main__":
    generate_mock_wearable_data()
