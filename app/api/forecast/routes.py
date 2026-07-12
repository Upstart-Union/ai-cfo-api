from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"],
)

class ForecastRequest(BaseModel):
    revenue: float
    expenses: float
    profit: float
    profit_margin: float

@router.post("")
def forecast(data: ForecastRequest):
    revenue = data.revenue
    expenses = data.expenses

    return {
        "success": True,
        "forecast": {
            "months": [
                "Jan",
                "Feb",
                "Mar",
                "Apr",
                "May",
                "Jun",
            ],
            "revenue": [
                revenue * 1.02,
                revenue * 1.04,
                revenue * 1.06,
                revenue * 1.08,
                revenue * 1.10,
                revenue * 1.12,
            ],
            "expenses": [
                expenses * 1.01,
                expenses * 1.02,
                expenses * 1.03,
                expenses * 1.04,
                expenses * 1.05,
                expenses * 1.06,
            ],
            "profit": [
                revenue * 1.02 - expenses * 1.01,
                revenue * 1.04 - expenses * 1.02,
                revenue * 1.06 - expenses * 1.03,
                revenue * 1.08 - expenses * 1.04,
                revenue * 1.10 - expenses * 1.05,
                revenue * 1.12 - expenses * 1.06,
            ],
        },
    }
