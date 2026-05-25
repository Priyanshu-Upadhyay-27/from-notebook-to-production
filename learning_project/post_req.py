from fastapi import FastAPI, Path, Query, HTTPException, Field
from pydantic import BaseModel
from typing import Annotated, Literal
import json

class Patient(BaseModel):
    id: Annotated[str, Field(..., description = "Id of the Patient", examples = ["P001"])]
    name: Annotated[str, Field(..., description = "Name of the Patient", examples = ["Ankit"])]
    city: Annotated[str, Field(..., description = "City of the Patient", examples = ["Agra", "Delhi"])]
    age: Annotated[int, Field(..., gt = 0, lt = 110, description = "Age of the Patient", examples = [27, 68])]
    gender: Annotated[Literal["male", "female", "others"], Field(..., description = "Gender of the patient", examples = ["male", "female", "others"])]
    height: Annotated[float, Field(..., gt = 0, description = "Height of the patient(in meter)", examples = [1.72, 1.67] )]
    weight: Annotated[float, Field(..., gt = 0, description = "Weight pf the patient(in Kg)", examples = [75, 68])]



app1 = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data