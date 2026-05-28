from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Optional, Annotated, Literal
import pandas as pd
import joblib

# Import model
model = joblib.load("titanic_svm_pipeline.pkl")

app = FastAPI()

