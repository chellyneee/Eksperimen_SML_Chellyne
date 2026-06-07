import requests
import asyncio
import json
from fastapi import FastAPI
 
app = FastAPI()
 
MLFLOW_MODEL_URL = "http://127.0.0.1:8000/predict"  # URL endpoint model MLflow
 
async def async_infer(data):
    """Melakukan inferensi secara asinkron ke MLflow Model Serving."""
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"instances": data})
 
    async def request_model():
        response = requests.post(MLFLOW_MODEL_URL, headers=headers, data=payload)
        return response.json()
 
    return await asyncio.to_thread(request_model)
 
@app.post("/predict")
async def predict(data: dict):
    """Endpoint FastAPI untuk menangani inferensi secara asinkron."""
    task = asyncio.create_task(async_infer(data["input"]))
    return {"status": "processing", "task_id": id(task)}