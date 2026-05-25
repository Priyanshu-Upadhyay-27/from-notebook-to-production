from fastapi import FastAPI, Path, Query, HTTPException
import json

app1 = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data