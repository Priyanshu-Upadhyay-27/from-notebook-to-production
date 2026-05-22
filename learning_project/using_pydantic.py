from pydantic import BaseModel

class validate_patient_data(BaseModel):
    name: str
    age: int

def insert_patient_data(patient: validate_patient_data):
    print(patient.name)
    print(patient.age)
    print("Inserted")

patient_info = {"name":"Priyanshu", "age":30}

patient1 = validate_patient_data(**patient_info)

insert_patient_data(patient1)