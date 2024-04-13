#!/usr/bin/env python3
"""
Created on Sat Apr 13 11:24:33 2024.

@author: Tristan Muscat
"""

import pandas as pd
from sqlalchemy import create_engine

import mlflow

# Import data
engine = create_engine('postgresql://postgres:admin@localhost:5432/postgres')

df = pd.read_sql("wine", engine)

mlflow.set_tracking_uri("http://localhost:5000/")

MODEL_NAME = "wine_quality"
MODEL_VERSION = "production"
model_uri = f"models:/{MODEL_NAME}@{MODEL_VERSION}"
model = mlflow.sklearn.load_model(model_uri)

score = model.score(df.drop(columns=["quality"]), df[["quality"]])

print(f"Score du model : {score}")
