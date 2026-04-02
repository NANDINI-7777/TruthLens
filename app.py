from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Deep Learning Fake News Detector API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Downloading and loading the Deep Learning model... This might take a minute!")
# This downloads a specific BERT model fine-tuned on 40,000+ real and fake news articles.
# truncation=True ensures the AI doesn't crash if you paste a massive 10-page article.
fake_news_ai = pipeline("text-classification", model="jy46604790/Fake-News-Bert-Detect", truncation=True, max_length=512)

class NewsInput(BaseModel):
    text: str

@app.post("/predict")
def predict_news(news: NewsInput):
    # The Hugging Face pipeline reads the text and returns a label and score instantly
    prediction_result = fake_news_ai(news.text)[0]
    
    label = prediction_result['label']
    confidence = prediction_result['score'] * 100
    
    # This specific model outputs 'LABEL_0' for Fake and 'LABEL_1' for Real
    if label == "LABEL_0":
        result = "Fake News"
    else:
        result = "Real News"
    
    return {
        "prediction": result,
        "confidence": f"{confidence:.2f}%"
    }