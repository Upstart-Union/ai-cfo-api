from fastapi import APIRouter

from pydantic import BaseModel

from app.services.ai.llm_service import (
    chat,
    generate_summary,
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"],
)


class SummaryRequest(BaseModel):
    revenue: float
    expenses: float
    profit: float
    profit_margin: float


class ChatRequest(BaseModel):
    message: str
    dashboard: dict | None = None


@router.post("/summary")
def summary(data: SummaryRequest):
    print("===== SUMMARY REQUEST =====")

    return {
        "summary": generate_summary(
            data.model_dump()
        )
    }


@router.post("/chat")
def chat_route(data: ChatRequest):
    print("===== CHAT REQUEST =====")

    return {
        "answer": chat(
            data.message,
            data.dashboard,
        )
    }
