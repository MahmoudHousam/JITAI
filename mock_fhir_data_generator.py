import json
from datetime import datetime, timedelta
import random


def generate_mock_fhir_data(num_patients=100):
    fhir_data = []
    for i in range(1, num_patients + 1):
        patient = {
            "patient_id": f"P{i:03d}",  # P001, P002, etc.
            "name": f"Patient {i}",
            "age": random.randint(20, 80),
            "gender": random.choice(["Male", "Female"]),
            "diagnosis": random.choice(["Diabetes", "Hypertension", "Depression"]),
            "medication": random.choice(["Metformin", "Amlodipine", "SSRI"]),
            "last_medication_dose": (
                datetime.now() - timedelta(hours=random.randint(1, 24))
            ).isoformat()
            + "Z",
            "last_lab_result": {
                "glucose_level": (
                    random.randint(70, 200) if random.choice([True, False]) else None
                ),
                "blood_pressure": (
                    f"{random.randint(110, 140)}/{random.randint(70, 90)}"
                    if random.choice([True, False])
                    else None
                ),
                "timestamp": (
                    datetime.now() - timedelta(hours=random.randint(1, 24))
                ).isoformat()
                + "Z",
            },
        }
        fhir_data.append(patient)
    return fhir_data


def save_mock_data(fhir_data):
    with open("mock_fhir_data.json", "w") as f:
        json.dump(fhir_data, f, indent=4)


if __name__ == "__main__":
    fhir_data = generate_mock_fhir_data()
    save_mock_data(fhir_data)
