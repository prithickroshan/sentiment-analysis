from transformers import pipeline
from typing import List

# Load model once at startup
print("Loading DistilBERT model...")
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
    return_all_scores=True
)
print("Model loaded successfully ✅")

# Threshold below which we consider sentiment NEUTRAL
NEUTRAL_THRESHOLD = 0.75


def _map_result(text: str, raw: list) -> dict:
    """
    Maps raw DistilBERT scores to POSITIVE / NEGATIVE / NEUTRAL.
    If the top score is below NEUTRAL_THRESHOLD, classify as NEUTRAL.
    """
    scores = {item["label"]: round(item["score"], 4) for item in raw}

    top_label = max(scores, key=scores.get)
    top_score = scores[top_label]

    if top_score < NEUTRAL_THRESHOLD:
        sentiment = "NEUTRAL"
        confidence = round(1 - abs(scores.get("POSITIVE", 0) - scores.get("NEGATIVE", 0)), 4)
    else:
        sentiment = top_label  # POSITIVE or NEGATIVE
        confidence = top_score

    scores["NEUTRAL"] = round(1 - top_score, 4) if sentiment != "NEUTRAL" else confidence

    return {
        "text": text,
        "sentiment": sentiment,
        "confidence": confidence,
        "scores": scores,
    }


def predict_sentiment(text: str) -> dict:
    raw = classifier(text)[0]
    return _map_result(text, raw)


def predict_batch(texts: List[str]) -> List[dict]:
    raw_batch = classifier(texts)
    return [_map_result(text, raw) for text, raw in zip(texts, raw_batch)]
