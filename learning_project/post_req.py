from fastapi import FastAPI, Path, Query, HTTPException, Field
from pydantic import BaseModel, computed_field
from typing import Annotated, Literal
import json

app1 = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description = "Id of the Patient", examples = ["P001"])]
    name: Annotated[str, Field(..., description = "Name of the Patient", examples = ["Ankit"])]
    city: Annotated[str, Field(..., description = "City of the Patient", examples = ["Agra", "Delhi"])]
    age: Annotated[int, Field(..., gt = 0, lt = 110, description = "Age of the Patient", examples = [27, 68])]
    gender: Annotated[Literal["male", "female", "others"], Field(..., description = "Gender of the patient", examples = ["male", "female", "others"])]
    height: Annotated[float, Field(..., gt = 0, description = "Height of the patient(in meter)", examples = [1.72, 1.67] )]
    weight: Annotated[float, Field(..., gt = 0, description = "Weight pf the patient(in Kg)", examples = [75, 68])]

    @computed_field()
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'underweight'
        elif self.bmi < 25:
            return 'normal'
        elif self.bmi < 30:
            return 'overweight'
        else:
            return 'obese'
        

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data