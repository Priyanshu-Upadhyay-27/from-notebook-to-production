from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated
class validate_patient_data(BaseModel):
    name: Annotated[str, Field(max_length=20, title="Name of the Patient", 
                               description="Enter the name of the patient and it should be smaller then 20 characters.",
                               examples = ["Nitish", "Priyanshuu"])]
    email: EmailStr # It can validate the format of email is correct or not.
    linkedin_url: AnyUrl # It can validate any URL.
    age: int = Field(ge=0, lt = 100)
    weight: float 
    married: Annotated[bool, Field(default = False, description="Enter the marriage status of the partner", 
                                   title = "Married or Not", examples= "True or False")]
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]


def insert_patient_data(patient: validate_patient_data):
    print(f"Patient Name: {patient.name}")
    print(f"Patients Contact info: {patient.email}")
    print(f"Patient's LinkedIn: {patient.linkedin_url}")
    print(f"patient Age: {patient.age}")
    print(f"Weight of the patient: {patient.weight}")
    print(f"Is the Patient Married: {patient.married}")
    print(f"Allergies in the patient:{patient.allergies}")
    print(f"Contact Details: {patient.contact_details}")
    print("Inserted")

patient_info = {"name":"Priyanshuuuuu", "email": "abc@gmail.com", "age":"-30", "weight": 80.3, "married":True,
                 "allergies":["Pollen", "dogs", "bees", "dust"], "linkedin_url": "https://www.linkedin.com/in/priyanshu-upadhyay-cse/",
                 "contact_details":{"phone no.:":"9730735220"}} # here pydantic is converting, string 30 into integer 30.

patient1 = validate_patient_data(**patient_info)

insert_patient_data(patient1)