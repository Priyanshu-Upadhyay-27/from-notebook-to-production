from pydantic import BaseModel

class Address(BaseModel):
    house_number: int
    street: str
    area: str
    district: str
    state: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address

address_info = {"house_number":1175, "street": "Gandhi Street", "area": "Mahavidhya Colony", "district": "Agra", "state": "Uttar Pradesh"}
address1 = Address(**address_info)

patient_info = {"name": "priyanshu", "age":45, "gender": "male", "address":address1}
patient1 = Patient(**patient_info)

print(patient1.name)
print(patient1.age)
print(patient1.address.house_number)
print(patient1.address.district)


# Better Organisation 
# Reusable
# Readable
# Automatic Validation