from fastapi import FastAPI, Path, HTTPException, Query
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
def get_patient_data(patient_id: str = Path(..., description="Id of the Patient in the database", examples ="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient Not Found")
    

@app.get("/sort")
def patient_sort(sort_by: str = Query(description = "Sort on the basis of height, weight or bmi"), 
                 order: str = Query(description = "Sorting in asc and desc")):
    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail = f"Invalid field, select from {valid_fields}")
    
    if order not in["asc", "desc"]:
        raise HTTPException(status_code = 400, detail = "Invalid field, select from asc or desc")
    
    data = load_data()
    sort_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse = sort_order)

    return sorted_data
    
