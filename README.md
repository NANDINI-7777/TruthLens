# 🔮 TruthLens — AI Fake News Detector

TruthLens is a full-stack, AI-powered web application designed to detect misinformation and classify news articles or headlines as **Real** or **Fake**. 

The app features a custom glassmorphism design panel, live progress scanning visuals, and dynamic metric bars assessing source credibility, emotional tone, and factual consistency.

---

## 🚀 The Journey: From Baseline to Deep Learning

I initially built this project using a standard **TF-IDF Vectorizer and Logistic Regression** model. However, I quickly discovered the limitations of basic NLP (such as dataset word memorization) where the model was simply memorizing specific terms rather than understanding the deep context of sentences.

To solve this, I upgraded the backend engine to use **Deep Learning**. TruthLens is now powered by a **Hugging Face Transformer (BERT)** model (`jy46604790/Fake-News-Bert-Detect`), allowing it to analyze bidirectional context and grammatical structure, drastically improving its accuracy on real-world news snippets.

---

## ⚡ Lightweight Vercel-Ready Refactor

Originally, this project loaded a heavy 1.5GB BERT model locally inside a Python FastAPI backend using `torch` and `transformers`. While great for offline runs, this is **not compatible with Vercel serverless functions** due to Vercel's strict 250MB free-tier bundle limit.

To enable **seamless, free, and global hosting on Vercel**, the backend has been refactored into a **lightweight API proxy** (`api/index.py`):
*   Instead of running the heavy BERT model inside Vercel, the backend forwards the news text to the **free Hugging Face Inference API**.
*   This drops your deployment size from **1.5GB to under 20MB**, bypassing all cold-starts.
*   Results return in under **200 milliseconds**!
*   The application works perfectly both offline locally and hosted live on Vercel under a single relative route (`/api/predict`), completely avoiding all CORS issues!

---

## 🛠️ Technology Stack

*   **Frontend:** HTML5, CSS3, Vanilla JavaScript (Modern Glassmorphic UI)
*   **Backend Proxy:** Python, FastAPI, Requests, Uvicorn
*   **Deep Learning Model:** Hugging Face BERT (`jy46604790/Fake-News-Bert-Detect`)
*   **Hosting & Serverless:** Vercel

---

## 📦 How to Run Locally

### Prerequisites
Make sure you have [Node.js](https://nodejs.org/) (for static hosting or package running) and [Python 3.9+](https://www.python.org/) installed.

### 1. Initialize Python Backend
1. Open your terminal in the `fake_news_detector` folder.
2. Install the lightweight dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the FastAPI local server:
   ```bash
   python app.py
   ```
   *(The server will start running on `http://127.0.0.1:8000`).*

### 2. Run the Frontend
*   Simply double-click the **`index.html`** file in your explorer to open it in any browser, or use a local static server like Live Server.
*   The frontend is configured with a dynamic endpoint resolver—it will automatically detect that you are running locally and connect to your local FastAPI server on port 8000!

---

## 🚀 Quick Vercel Deployment

TruthLens is configured for a single-click Vercel deployment:

1. Import your `fake_news_detector` repository into your **[Vercel Dashboard](https://vercel.com/new)**.
2. Vercel will automatically detect the static frontend (`index.html`) and the Python serverless function (`api/index.py`).
3. *(Optional)* Under **Environment Variables**, you can add a free Hugging Face API key:
   *   **Name**: `HF_TOKEN`
   *   **Value**: *Your Hugging Face Read Token* (Optional, but helps prevent rate limits).
4. Click **"Deploy"**!

---

## 👩‍💻 Made By
Developed with ♥ by **Nandini Soni**. Let's connect!
*   **LinkedIn**: [Nandini Soni](https://www.linkedin.com/in/nandini-soni-89817029a?utm_source=share_via&utm_content=profile&utm_medium=member_android)
*   **Email**: [nandinisoni7014@gmail.com](mailto:nandinisoni7014@gmail.com)
*   **GitHub**: [Nandini Soni](https://github.com/NANDINI-7777)