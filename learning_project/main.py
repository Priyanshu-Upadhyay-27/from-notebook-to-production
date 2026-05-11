from fastapi import FastAPI
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