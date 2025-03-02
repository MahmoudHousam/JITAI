import json
from datetime import datetime
from fhir.resources.patient import Patient
from fhir.resources.condition import Condition
from fhir.resources.observation import Observation
from fhir.resources.medicationstatement import MedicationStatement


def create_diabetic_hypertensive_resource():
    # Patient Resource
    patient = Patient.model_construct()
    patient.id = "samer-123"
    patient.gender = "male"
    patient.birthDate = "1980-05-15"
    patient.extension = [
        {
            "url": "http://scrips.com/fhir/clinical-summary",
            "valueString": "Type 2 Diabetes (E11.9), Hypertension (I10)",
        }
    ]

    # Condition: Diabetes
    condition = Condition.model_construct()
    condition.id = "condition-1"
    condition.code = {
        "coding": [
            {
                "system": "http://hl7.org/fhir/sid/icd-10",
                "code": "E11.9",
                "display": "Type 2 Diabetes Mellitus",
            }
        ]
    }
    condition.subject = {"reference": "Patient/samer-123"}
    condition.clinicalStatus = {
        "coding": [
            {
                "system": "http://terminology.hl7.org/CodeSystem/condition-clinical",
                "code": "active",
                "display": "Active",
            }
        ]
    }

    # Glucose Observation
    glucose = Observation.model_construct(
        id="glucose-1",
        status="final",
        code={
            "coding": [
                {"system": "http://loinc.org", "code": "2339-0", "display": "Glucose"}
            ]
        },
        subject={"reference": "Patient/samer-123"},
        effectiveDateTime="2023-10-05T08:00:00Z",
        valueQuantity={
            "value": 210,
            "unit": "mg/dL",
            "system": "http://unitsofmeasure.org",
        },
        extension=[
            {"url": "http://scrips.com/fhir/severity", "valueDecimal": 0.4},
            {"url": "http://scrips.com/fhir/weight", "valueDecimal": 0.8},
        ],
    )

    # Missed SSRI Medication
    med = MedicationStatement.model_construct(
        id="med-1",
        status="active",
        medication={
            "coding": [
                {
                    "system": "http://www.nlm.nih.gov/research/umls/rxnorm",
                    "code": "329526",
                    "display": "Sertraline",
                }
            ]
        },
        subject={"reference": "Patient/samer-123"},
        taken="n",
        effectivePeriod={"start": "2023-10-05T08:00:00Z"},
    )
    return [patient, condition, glucose, med]


# Convert to JSON
samer_resources = [
    resource.dict() for resource in create_diabetic_hypertensive_resource()
]
print(samer_resources)
# with open("mock_fhir_data/diabetic_hypertensive.json", "w") as f:
#     json.dump(samer_resources, f, indent=4)
