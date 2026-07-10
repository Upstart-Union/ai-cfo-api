def calculate_metrics(df):
    """
    Calculate simple financial metrics from uploaded data.

    Expected columns:
    Revenue
    Expenses
    """

    revenue = float(df["Revenue"].sum())

    expenses = float(df["Expenses"].sum())

    profit = revenue - expenses

    if revenue > 0:
        margin = round((profit / revenue) * 100, 2)
    else:
        margin = 0

    return {
        "revenue": revenue,
        "expenses": expenses,
        "profit": profit,
        "profit_margin": margin,
    }