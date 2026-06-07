import requests
import json
import time
import logging

logging.basicConfig(
    filename="api_model_logs.log", 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# API_URL = "http://127.0.0.1:5006/invocations"
API_URL = "http://127.0.0.1:8000/predict"

input_data = {
    "dataframe_split": {
        "columns": [
            "User_Id", 
            "Place_Id", 
            "Place_Ratings", 
            "Price", 
            "Rating", 
            "Lat", 
            "Long", 
            "City_Encoded", 
            "Age_Group_Encoded", 
            "Price_Scaled"
        ],
        "data": [
            [1, 101, 4, 150000, 4.5, -7.250444, 112.768845, 0, 2, 0.35]
        ]
    }
}

headers = {"Content-Type": "application/json"}
payload = json.dumps(input_data)

start_time = time.time()

try:
    response = requests.post(API_URL, headers=headers, data=payload)
    response_time = time.time() - start_time

    if response.status_code == 200:
        prediction = response.json()
        logging.info(f"Request: {input_data}, Response: {prediction}, Response Time: {response_time:.4f} sec")
        print(f"Prediction: {prediction}")
        print(f"Response Time: {response_time:.4f} sec")
    else:
        logging.error(f"Error {response.status_code}: {response.text}")
        print(f"Error {response.status_code}: {response.text}")

except Exception as e:
    logging.error(f"Exception: {str(e)}")
    print(f"Exception: {str(e)}")