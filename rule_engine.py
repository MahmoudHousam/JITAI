import json

# Load JSON data for Samer, Layla, and Ali
with open("diabetic_high_risk_glucose_spikes.json") as f:
    diabetic_high_risk_glucose_spikes = json.load(f)
with open("heart_failure_low_hrv.json") as f:
    heart_failure_low_hrv = json.load(f)
with open("hypertensive_missed_medication.json") as f:
    hypertensive_missed_medication = json.load(f)

# Define weighting factors
WEIGHTS = {
    "hrv": 0.9,
    "glucose": 0.8,
    "medication": 1.0,
    "sedentary": 0.6,
    "social": 0.7,
}

# Diagnosis-specific risk multipliers
DIAGNOSIS_MULTIPLIERS = {
    "E11.9": 1.5,  # Diabetes increases glucose risk
    "I50.9": 2.0,  # Heart failure increases HRV risk
    "I10": 1.2,  # Hypertension increases BP risk
}


# Extract diagnoses from Condition resources
def get_diagnoses(patient_data):
    diagnoses = []
    for resource in patient_data:
        if resource["resourceType"] == "Condition":
            code = resource["code"]["coding"][0]["code"]
            diagnoses.append(code)
    return diagnoses


# Event detection and nudge logic
def detect_events(patient_data, diagnoses):
    nudges = []
    for resource in patient_data:
        if resource["resourceType"] == "Observation":
            # HRV drop >30%
            if resource["code"]["coding"][0]["code"] == "8867-4":  # HRV
                hrv_value = resource["valueQuantity"]["value"]
                if hrv_value < 30:  # Example threshold
                    severity = resource["extension"][0]["valueDecimal"]
                    risk_score = severity * WEIGHTS["hrv"]
                    # Increase risk for heart failure patients
                    if "I50.9" in diagnoses:
                        risk_score *= DIAGNOSIS_MULTIPLIERS["I50.9"]
                    nudges.append(
                        {
                            "patient": resource["subject"]["reference"],
                            "message": f"HRV dropped to {hrv_value} ms. Consider resting.",
                            "risk_score": risk_score,
                        }
                    )
            # Glucose spike
            elif resource["code"]["coding"][0]["code"] == "2339-0":  # Glucose
                glucose_value = resource["valueQuantity"]["value"]
                if glucose_value > 200:  # Example threshold
                    severity = resource["extension"][0]["valueDecimal"]
                    risk_score = severity * WEIGHTS["glucose"]
                    # Increase risk for diabetic patients
                    if "E11.9" in diagnoses:
                        risk_score *= DIAGNOSIS_MULTIPLIERS["E11.9"]
                    nudges.append(
                        {
                            "patient": resource["subject"]["reference"],
                            "message": f"Glucose level is {glucose_value} mg/dL. Monitor your diet.",
                            "risk_score": risk_score,
                        }
                    )
        # Missed medication
        elif resource["resourceType"] == "MedicationStatement":
            if resource["taken"] == "n":  # Missed dose
                risk_score = 1.0 * WEIGHTS["medication"]  # Max weight
                nudges.append(
                    {
                        "patient": resource["subject"]["reference"],
                        "message": "You missed a medication dose. Please take it soon.",
                        "risk_score": risk_score,
                    }
                )
    return nudges


diabetic_diagnosis = get_diagnoses(diabetic_high_risk_glucose_spikes)
heart_failure_diagnosis = get_diagnoses(heart_failure_low_hrv)
hypertensive_diagnosis = get_diagnoses(hypertensive_missed_medication)

diabetic_nudges = detect_events(diabetic_high_risk_glucose_spikes, diabetic_diagnosis)
heart_failure_nudges = detect_events(heart_failure_low_hrv, heart_failure_diagnosis)
hypertensive_nudges = detect_events(
    hypertensive_missed_medication, hypertensive_diagnosis
)


print("Patient abc-123 Nudges:", diabetic_nudges)
print("Patient def-456 Nudges:", heart_failure_nudges)
print("Patient ghi-789 Nudges:", hypertensive_nudges)
