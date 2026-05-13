from fastapi import FastAPI, Path
import json

def load_data():
    with open("patients.json", "r") as file:
        data = json.load(file)
        return data

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Patient management system API"}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage patient records."}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def get_patient_data(patient_id: str = Path(..., description="Id of the Patient in the database", example ="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        return {"error": "Patient not found"}