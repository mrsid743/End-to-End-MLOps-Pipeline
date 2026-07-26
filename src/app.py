from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mlflow.sklearn
import pandas as pd
import os

app = FastAPI(title="MLOps Iris Predictor")

# Load the model at startup
os.environ["MLFLOW_TRACKING_URI"] = os.environ.get("MLFLOW_TRACKING_URI", "http://127.0.0.1:5000")
MODEL_NAME = "IrisClassifier"
MODEL_VERSION = "1"

try:
    # Attempt to load Version 1 directly to bypass Stage/Alias issues
    model_uri = f"models:/{MODEL_NAME}/{MODEL_VERSION}"
    print(f"Loading model from: {model_uri}")
    model = mlflow.sklearn.load_model(model_uri)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model from MLflow: {e}")
    print("Falling back to local model if available, or API will fail.")
    model = None

class PredictRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(request: PredictRequest):
    if model is None:
        raise HTTPException(status_code=500, detail="Model could not be loaded.")
    
    # Format input for sklearn
    data = pd.DataFrame([{
        "sepal length (cm)": request.sepal_length,
        "sepal width (cm)": request.sepal_width,
        "petal length (cm)": request.petal_length,
        "petal width (cm)": request.petal_width
    }])
    
    try:
        prediction = model.predict(data)
        # Iris target names are typically: 0: setosa, 1: versicolor, 2: virginica
        class_names = ["setosa", "versicolor", "virginica"]
        pred_class = class_names[int(prediction[0])]
        
        return {"prediction": pred_class, "class_index": int(prediction[0])}
    except Exception as e:
         raise HTTPException(status_code=400, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": model is not None}