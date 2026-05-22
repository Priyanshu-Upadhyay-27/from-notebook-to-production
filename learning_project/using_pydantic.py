from pydantic import BaseModel
from typing import List, Dict
class validate_patient_data(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


def insert_patient_data(patient: validate_patient_data):
    print(f"Patient Name: {patient.name}")
    print(f"patient Age: {patient.age}")
    print(f"Weight of the patient: {patient.weight}")
    print(f"Is the Patient Married: {patient.married}")
    print(f"Allergies in the patient:{patient.allergies}")
    print(f"Contact Details: {patient.contact_details}")
    print("Inserted")

patient_info = {"name":"Priyanshu", "age":"30", "weight": 80.3, "married":True,
                 "allergies":["Pollen", "dogs", "bees", "dust"], "contact_details":{"email":"xyz@gmail.com", "phone no.:":"9730735220"}} # here pydantic is converting, string 30 into integer 30.

patient1 = validate_patient_data(**patient_info)

insert_patient_data(patient1)