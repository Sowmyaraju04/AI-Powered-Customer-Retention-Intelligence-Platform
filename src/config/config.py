"""
Configuration Module

Project:
AI-Powered Customer Retention Intelligence Platform
"""

from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Data Paths
DATA_PATH = PROJECT_ROOT / "data"

RAW_DATA_PATH = DATA_PATH / "raw"

PROCESSED_DATA_PATH = DATA_PATH / "processed"

CLEANED_DATA_PATH = DATA_PATH / "cleaned"

FINAL_DATA_PATH = DATA_PATH / "final"

# Reports
REPORTS_PATH = PROJECT_ROOT / "reports"

# Models
MODELS_PATH = PROJECT_ROOT / "src" / "models"