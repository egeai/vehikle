#!/bin/bash


# Run launcher.py
python launcher.py

# Start FastAPI
uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload