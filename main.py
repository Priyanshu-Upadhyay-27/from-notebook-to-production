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

@app.get("/student/{student_id}/subject/{subject_name}")
def get_subject(student_id: int, subject_name: str):
    return {
        "student_id": student_id,
        "subject": subject_name
    }

"""@app.get("/students")
def get_students(city: str, age: int):
    return {
        "city": city,
        "age": age,
        "message": f"Fetching students from {city} aged {age}"
    }"""
from typing import Optional

@app.get("/students")
def get_students(city: str, age: Optional[int] = None):
    if age:
        return {"city": city, "age": age}
    return {"city": city, "age": "not provided"}

@app.get("/student/{student_id}/results")
def get_results(student_id: int, subject: Optional[str] = None):
    if subject:
        return {"student_id": student_id, "subject": subject}
    return {"student_id": student_id, "subject": "all subjects"}


