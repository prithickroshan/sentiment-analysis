from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import PredictRequest, PredictResponse, BatchRequest, BatchResponse
from app.model import predict_sentiment, predict_batch

app = FastAPI(
    title="Sentiment Analysis API",
    description="A production-ready REST API for sentiment analysis using DistilBERT. Built by Prithick Roshan S.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
def root():
    return {
        "message": "Sentiment Analysis API is running 🚀",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health", tags=["Health"])
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse, tags=["Prediction"])
def predict(request: PredictRequest):
    """
    Predict sentiment of a single text input.
    Returns POSITIVE, NEGATIVE, or NEUTRAL with confidence score.
    """
    result = predict_sentiment(request.text)
    return result


@app.post("/predict/batch", response_model=BatchResponse, tags=["Prediction"])
def predict_batch_endpoint(request: BatchRequest):
    """
    Predict sentiment for multiple texts at once.
    """
    results = predict_batch(request.texts)
    return BatchResponse(results=results)
