#!/usr/bin/env python3
"""
Created on Sat Apr 06 15:09:04 2024.

@author: Tristan Muscat
"""

import pandas as pd
from fastapi import FastAPI
from sqlalchemy import create_engine

from api_wine.data_models import WineInput
from api_wine.settings import get_settings

import mlflow

settings = get_settings()

app = FastAPI()

mlflow.set_tracking_uri(f"http://{settings.MLFLOW_HOST}:5000/")

MODEL_NAME = "wine_quality"
MODEL_VERSION = "production"
MODEL_URI = f"models:/{MODEL_NAME}@{MODEL_VERSION}"
MODEL = mlflow.sklearn.load_model(MODEL_URI)


@app.get("/")
async def root():
    """Create root endpoint for the API"""
    return {"message": "ok"}


@app.get("/model")
async def get_model():
    """Display model"""
    return str(MODEL)


@app.post("/quality")
async def get_wine_quality(input: WineInput):
    """Predict the quality of a wine based on its attributes."""
    df = pd.json_normalize(input.__dict__)

    pred = MODEL.predict(df)
    print(pred)

    return {"prediction": pred[0]}
