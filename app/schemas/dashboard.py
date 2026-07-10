from pydantic import BaseModel


class DashboardResponse(BaseModel):
    revenue: float
    expenses: float
    profit: float
    profit_margin: float