from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}

@app.get("/student/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id, "message": f"Fetching student {student_id}"}

