import random
import json
from datetime import datetime, timedelta


def generate_mock_fhir_data(num_patients):
    fhir_data = []
    for i in range(1, num_patients + 1):
        medications = [
            "Fluoxetine",
            "Sertraline",
            "Escitalopram",
            "Venlafaxine",
            "Bupropion",
        ]

        patient = {
            "patient_id": f"P{i:03d}",
            "name": f"Patient {i}",
            "age": random.randint(18, 70),  # Depression can affect all adults
            "gender": random.choice(["Male", "Female"]),
            "diagnosis": "Depression",
            "medication": random.choice(medications),
            "last_medication_dose": (
                datetime.now() - timedelta(hours=random.randint(1, 24))
            ).isoformat()
            + "Z",
            "last_lab_result": {
                "phq9_score": (
                    random.randint(10, 27) if random.choice([True, False]) else None
                ),
                "timestamp": (
                    datetime.now() - timedelta(hours=random.randint(1, 24))
                ).isoformat()
                + "Z",
            },
        }
        fhir_data.append(patient)
    with open("mock_data/fhir_data.json", "w") as f:
        json.dump(fhir_data, f, indent=4)


if __name__ == "__main__":
    generate_mock_fhir_data(num_patients=12)
