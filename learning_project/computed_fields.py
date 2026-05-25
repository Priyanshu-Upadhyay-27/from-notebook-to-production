from pydantic import BaseModel, Field, computed_field, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age:int
    height:float # meters
    weight:float # Kgs
    married:bool
    allergies:List[str]
    contact_details:Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight/self.height, 2)
        return bmi

        
def insert_patient_data(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patients Email info: {patient.email}")
    print(f"patient Age: {patient.age}")
    print(f"Weight of the patient: {patient.weight}")
    print(f"BMI: {patient.calculate_bmi}")
    print(f"Is the Patient Married: {patient.married}")

patient_info = {"name":"Priyanshuuuuu", "email": "abc@icici.com", "age":"69", "weight": 80.3, "height":1.72, "married":True,
                 "allergies":["Pollen", "dogs", "bees", "dust"], "contact_details":{"phone no.:":"9730735220"}}

patient1 = Patient(**patient_info) 

insert_patient_data(patient1)



