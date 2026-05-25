from pydantic import BaseModel, Field, field_validator, model_validator, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str, str]

    @model_validator(mode = "after")
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Emergency contact is mandatory for people who are above 60.")
        return model

        
def insert_patient_data(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patients Email info: {patient.email}")
    print(f"patient Age: {patient.age}")
    print(f"Weight of the patient: {patient.weight}")
    print(f"Is the Patient Married: {patient.married}")

patient_info = {"name":"Priyanshuuuuu", "email": "abc@icici.com", "age":"69", "weight": 80.3, "married":True,
                 "allergies":["Pollen", "dogs", "bees", "dust"], "contact_details":{"phone no.:":"9730735220"}}

patient1 = Patient(**patient_info) 

insert_patient_data(patient1)



