# 🧠 Sentiment Analysis API

A **production-ready REST API** for sentiment analysis built with **FastAPI**, **DistilBERT**, and **Docker**.  
Classifies text as **POSITIVE**, **NEGATIVE**, or **NEUTRAL** with confidence scores.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111-green?logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker)
![HuggingFace](https://img.shields.io/badge/HuggingFace-DistilBERT-yellow?logo=huggingface)

---

## 📸 Demo

### ✅ API Response (Postman)
<!-- Add your Postman screenshot here -->
![Postman Demo](images/postman_demo.png)

### 🐳 Docker Running
<!-- Add your Docker terminal screenshot here -->
![Docker](images/docker_running.png)

### 📄 Swagger Docs (/docs)
<!-- Add your Swagger UI screenshot here -->
![Swagger](images/swagger_docs.png)

---

## 🚀 Features

- ⚡ **FastAPI** — async, high-performance REST API
- 🤗 **DistilBERT** — `distilbert-base-uncased-finetuned-sst-2-english`
- 🎯 **3-class output** — POSITIVE, NEGATIVE, NEUTRAL (via confidence threshold)
- 📦 **Batch prediction** — analyze multiple texts in one request
- 🐳 **Docker** — fully containerized, runs anywhere
- 📄 **Auto Docs** — Swagger UI at `/docs`, ReDoc at `/redoc`

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| API Framework | FastAPI |
| ML Model | DistilBERT (HuggingFace) |
| Language | Python 3.10 |
| Containerization | Docker |
| API Testing | Postman |

---

## 📁 Project Structure

```
sentiment-analysis-api/
├── app/
│   ├── __init__.py
│   ├── main.py        # FastAPI routes
│   ├── model.py       # DistilBERT loader & predictor
│   └── schemas.py     # Pydantic request/response models
├── images/            # Screenshots for README
├── .dockerignore
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Getting Started

### 🐳 Run with Docker (Recommended)

```bash
# Clone the repo
git clone https://github.com/prithickroshan/sentiment-analysis-api.git
cd sentiment-analysis-api

# Build the image
docker build -t sentiment-api .

# Run the container
docker run -d -p 8000:8000 sentiment-api
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 💻 Run Locally (without Docker)

```bash
# Clone the repo
git clone https://github.com/prithickroshan/sentiment-analysis-api.git
cd sentiment-analysis-api

# Create virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn app.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📡 API Endpoints

### `GET /health`
Health check.
```json
{ "status": "ok" }
```

---

### `POST /predict`
Predict sentiment of a single text.

**Request:**
```json
{
  "text": "I love building AI projects!"
}
```

**Response:**
```json
{
  "text": "I love building AI projects!",
  "sentiment": "POSITIVE",
  "confidence": 0.9987,
  "scores": {
    "POSITIVE": 0.9987,
    "NEGATIVE": 0.0013,
    "NEUTRAL": 0.0013
  }
}
```

---

### `POST /predict/batch`
Predict sentiment for multiple texts.

**Request:**
```json
{
  "texts": ["I love this!", "This is terrible.", "It is okay."]
}
```

**Response:**
```json
{
  "results": [
    { "text": "I love this!", "sentiment": "POSITIVE", "confidence": 0.9991, "scores": {...} },
    { "text": "This is terrible.", "sentiment": "NEGATIVE", "confidence": 0.9978, "scores": {...} },
    { "text": "It is okay.", "sentiment": "NEUTRAL", "confidence": 0.6821, "scores": {...} }
  ]
}
```

---

## 🧪 Test with cURL

```bash
# Single prediction
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{"text": "This API is amazing!"}'

# Batch prediction
curl -X POST "http://localhost:8000/predict/batch" \
  -H "Content-Type: application/json" \
  -d '{"texts": ["Great work!", "Terrible experience.", "It was okay."]}'
```

---

## 🧠 How NEUTRAL Works

DistilBERT outputs binary scores (POSITIVE / NEGATIVE).  
If the top confidence score is **below 0.75**, the text is classified as **NEUTRAL** — meaning the model isn't confident enough to lean either way.

| Score | Classification |
|-------|---------------|
| POSITIVE ≥ 0.75 | POSITIVE |
| NEGATIVE ≥ 0.75 | NEGATIVE |
| Top score < 0.75 | NEUTRAL |

---

## 👨‍💻 Author

**Prithick Roshan S**  
AI Engineer | Python Developer | LLM Application Builder

🔗 [LinkedIn](https://www.linkedin.com/in/prithickroshan) | 🐙 [GitHub](https://github.com/prithickroshan) | 📧 prithickr@gmail.com

---

⭐ **If this project helped you, give it a star!**
