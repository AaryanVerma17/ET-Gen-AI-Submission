from typing import Dict

def calculate_money_health_score(user_data: Dict[str, any]) -> Dict[str, any]:

    income = user_data.get("income", 0)
    expenses = user_data.get("expenses", 0)
    savings = user_data.get("savings", 0)
    investment = user_data.get("investment", 0)
    emi = user_data.get("emi", 0)
    insurance = user_data.get("insurance", "None")
    tax_utilization = user_data.get("tax_utilization", "None")

    # ===============================
    # 1. Savings Score (0–20)
    # ===============================
    savings_rate = (income - expenses) / income if income > 0 else 0

    if savings_rate >= 0.4:
        savings_score = 20
    elif savings_rate >= 0.25:
        savings_score = 15
    elif savings_rate >= 0.1:
        savings_score = 10
    else:
        savings_score = 5

    # ===============================
    # 2. Emergency Score (0–20)
    # ===============================
    months = savings / expenses if expenses > 0 else 0

    if months >= 6:
        emergency_score = 20
    elif months >= 3:
        emergency_score = 15
    elif months >= 1:
        emergency_score = 10
    else:
        emergency_score = 5

    # ===============================
    # 3. Investment Score (0–20)
    # ===============================
    invest_ratio = investment / income if income > 0 else 0

    if invest_ratio >= 0.3:
        investment_score = 20
    elif invest_ratio >= 0.15:
        investment_score = 15
    elif invest_ratio >= 0.05:
        investment_score = 10
    else:
        investment_score = 5

    # ===============================
    # 4. Debt Score (0–15)
    # ===============================
    emi_ratio = emi / income if income > 0 else 1

    if emi_ratio < 0.2:
        debt_score = 15
    elif emi_ratio < 0.4:
        debt_score = 10
    else:
        debt_score = 5

    # ===============================
    # 5. Insurance Score (0–15)
    # ===============================
    if insurance == "Health + Term":
        insurance_score = 15
    elif insurance in ["Health", "Term"]:
        insurance_score = 10
    else:
        insurance_score = 5

    # ===============================
    # 6. Tax Score (0–10)
    # ===============================
    if tax_utilization == "Full":
        tax_score = 10
    elif tax_utilization == "Partial":
        tax_score = 7
    else:
        tax_score = 3

    # ===============================
    # FINAL OUTPUT
    # ===============================
    categoryScores = {
        "savings": savings_score,
        "emergency": emergency_score,
        "investment": investment_score,
        "debt": debt_score,
        "insurance": insurance_score,
        "tax": tax_score,
    }

    totalScore = sum(categoryScores.values())

    return {
        "totalScore": totalScore,
        "categoryScores": categoryScores
    }