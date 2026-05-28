import os
import requests
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="TruthLens - AI Fake News Detector Proxy API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class NewsInput(BaseModel):
    text: str

@app.post("/api/predict")
@app.post("/predict")  # Retain backward compatibility for local uvicorn runs
def predict_news(news: NewsInput):
    # Hugging Face Inference API Model URL
    model_url = "https://api-inference.huggingface.co/models/jy46604790/Fake-News-Bert-Detect"
    
    headers = {}
    # Retrieve optional HF Token from environment variables
    hf_token = os.environ.get("HF_TOKEN")
    if hf_token:
        headers["Authorization"] = f"Bearer {hf_token}"
        
    try:
        response = requests.post(model_url, headers=headers, json={"inputs": news.text}, timeout=15)
        
        if response.status_code != 200:
            error_msg = f"Hugging Face API returned error status {response.status_code}"
            try:
                error_msg += f": {response.text}"
            except:
                pass
            raise HTTPException(status_code=502, detail=error_msg)
            
        data = response.json()
        
        # Hugging Face inference pipeline response format is typically nested:
        # [[{"label": "LABEL_0", "score": 0.95}, {"label": "LABEL_1", "score": 0.05}]]
        if not data or not isinstance(data, list) or not isinstance(data[0], list):
            raise HTTPException(status_code=502, detail="Invalid response structure from Hugging Face Inference API.")
            
        predictions = data[0]
        
        # Find the label dictionary with the highest score
        top_prediction = max(predictions, key=lambda x: x.get('score', 0))
        
        label = top_prediction.get('label')
        confidence = top_prediction.get('score', 0) * 100
        
        # LABEL_0 is Fake News, LABEL_1 is Real News
        if label == "LABEL_0":
            result = "Fake News"
        else:
            result = "Real News"
            
        return {
            "prediction": result,
            "confidence": f"{confidence:.2f}%"
        }
    except requests.exceptions.Timeout:
        raise HTTPException(status_code=504, detail="The AI model took too long to respond. Please try again.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Proxy Error: {str(e)}")
