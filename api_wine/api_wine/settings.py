#!/usr/bin/env python3
"""
Created on Sat Apr 06 15:09:04 2024.

@author: Tristan Muscat
"""

import os
from functools import lru_cache

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    """Gather all settings for the Cat API."""

    MLFLOW_HOST: str = "localhost"


@lru_cache
def get_settings():
    return Settings()
