from pydantic import BaseModel

class validate_patient_data(BaseModel):
    name: str
    age: int
    weight: float

def insert_patient_data(patient: validate_patient_data):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("Inserted")

patient_info = {"name":"Priyanshu", "age":"30", "weight": 68.9} # here pydantic is converting, string 30 into integer 30.

patient1 = validate_patient_data(**patient_info)

insert_patient_data(patient1)