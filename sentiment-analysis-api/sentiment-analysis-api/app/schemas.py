from pydantic import BaseModel, Field
from typing import List


class PredictRequest(BaseModel):
    text: str = Field(..., example="I love building AI projects!", min_length=1)

    class Config:
        json_schema_extra = {
            "example": {
                "text": "I love building AI projects!"
            }
        }


class PredictResponse(BaseModel):
    text: str
    sentiment: str  # POSITIVE, NEGATIVE, NEUTRAL
    confidence: float
    scores: dict    # raw scores for all classes

    class Config:
        json_schema_extra = {
            "example": {
                "text": "I love building AI projects!",
                "sentiment": "POSITIVE",
                "confidence": 0.9987,
                "scores": {
                    "POSITIVE": 0.9987,
                    "NEGATIVE": 0.0013,
                    "NEUTRAL": 0.0
                }
            }
        }


class BatchRequest(BaseModel):
    texts: List[str] = Field(..., example=["I love this!", "This is terrible.", "It is okay."])


class BatchResponse(BaseModel):
    results: List[PredictResponse]
