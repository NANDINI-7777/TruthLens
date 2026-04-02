# TruthLens 🕵️‍♂️ - AI Fake News Detector

TruthLens is a full-stack, AI-powered web application designed to detect misinformation and classify news articles or headlines as Real or Fake. 

## 🚀 The Journey: From Baseline to Deep Learning
I initially built this project using a standard **TF-IDF Vectorizer and Logistic Regression** model. However, I quickly discovered the limitations of basic NLP (Dataset Bias) where the model was simply memorizing specific words rather than understanding the context of the sentence. 

To solve this, I upgraded the backend engine to use **Deep Learning**. TruthLens is now powered by a Hugging Face **Transformer (BERT)** model, allowing it to understand bidirectional context and grammar, drastically improving its accuracy on real-world news snippets.

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **Machine Learning:** Hugging Face `transformers`, PyTorch, pre-trained BERT model
* **Frontend:** HTML5, CSS3, Vanilla JavaScript (with a custom, responsive UI)

## ✨ Features
* **Real-time Inference:** Fast text-classification using a local FastAPI server.
* **Transformer Intelligence:** Context-aware predictions bypassing traditional keyword-bias.
* **Modern UI:** A sleek, responsive frontend featuring animated gauges, confidence scoring, and credibility metrics.

## ⚙️ How to Run Locally
1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies: `pip install fastapi uvicorn transformers torch pydantic`
4. Start the backend server: `uvicorn app:app --reload`
5. Open `index.html` in your web browser.