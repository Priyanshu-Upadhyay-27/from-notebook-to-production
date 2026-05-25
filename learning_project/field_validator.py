from pydantic import BaseModel, Field, field_validator, EmailStr, AnyUrl
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age:int
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ["hdfc.com", "icici.com"]
        domain_name = value.split("@")[-1]
        if domain_name in valid_domains:
            print(f"Person recognized from {domain_name}")
        else:
            raise ValueError("Not a valid domain")
        return value # retun value is very significant as the email will be None, if no return is there. 
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode = "before") # Custom data validation stage(second).
    @classmethod
    def validate_age(cls, value):
        if value not in range(1, 101):
            raise ValueError("Invalid Age")
        return value

        
def insert_patient_data(patient: Patient):
    print(f"Patient Name: {patient.name}")
    print(f"Patients Email info: {patient.email}")
    print(f"patient Age: {patient.age}")
    print(f"Weight of the patient: {patient.weight}")
    print(f"Is the Patient Married: {patient.married}")

patient_info = {"name":"Priyanshuuuuu", "email": "abc@icici.com", "age":"30", "weight": 80.3, "married":True,
                 "allergies":["Pollen", "dogs", "bees", "dust"], "contact_details":{"phone no.:":"9730735220"}}

patient1 = Patient(**patient_info) # Internal Data Validation Stage by pydantic (first), Internal Coercion happens here only.

insert_patient_data(patient1)



