#!/usr/bin/env python3
"""
Created on Sat Apr 13 10:38:53 2024.

@author: Tristan Muscat
"""

import sys
import pandas as pd
from sqlalchemy import create_engine

import mlflow

n_wine = 0
if len(sys.argv) >= 2:
    n_wine = int(sys.argv[1])


# Import data
engine = create_engine('postgresql://postgres:admin@localhost:5432/postgres')

df = pd.read_sql("wine", engine)

df.loc[n_wine].drop(columns=["quality"]).to_json("test.json", orient="index")
