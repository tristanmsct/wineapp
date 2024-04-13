#!/usr/bin/env python3
"""
Created on Sat Apr 13 11:24:33 2024.

@author: Tristan Muscat
"""

import pandas as pd
from sqlalchemy import create_engine

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
from sklearn.ensemble import RandomForestRegressor

from sklearn.model_selection import train_test_split

import mlflow

# Import data
engine = create_engine('postgresql://postgres:admin@localhost:5432/postgres')

df = pd.read_sql("wine", engine)

X_train, X_test, y_train, y_test = train_test_split(df.drop(columns=["quality"]), df[["quality"]], train_size=0.8)

mlflow.set_tracking_uri("http://localhost:5000/")

mlflow.autolog()

# Create pipeline
ml_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", RobustScaler()),
        ("regressor", RandomForestRegressor())
    ]
)

ml_pipeline.fit(X_train, y_train)

ml_pipeline.score(X_test, y_test)
