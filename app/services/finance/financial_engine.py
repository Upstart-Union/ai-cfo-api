from app.services.finance.metrics import (
    total_income,
    total_expenses,
    net_profit,
)

class FinancialEngine:

    def analyze(self, dataframe):
        return {
            "income": total_income(dataframe),
            "expenses": total_expenses(dataframe),
            "profit": net_profit(dataframe),
        }
