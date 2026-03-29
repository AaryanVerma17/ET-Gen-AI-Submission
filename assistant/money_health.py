def calculate_money_health_score(user_data: Dict[str, any]) -> Dict[str, any]:
    """
    Calculate Money Health Score and category breakdown from user_data.
    Returns a dict with totalScore and categoryScores.
    """
    answers = {}

    # Emergency preparedness: months of expenses saved
    try:
        months = user_data["savings"] / user_data["expenses"] if user_data["expenses"] > 0 else 0
    except Exception:
        months = 0
    answers["emergency_preparedness"] = str(int(months))

    # Insurance coverage: yes if both health and term insurance
    answers["insurance_coverage"] = "yes" if user_data.get("health_insurance") or user_data.get("term_insurance") else "no"

    # Investment diversification: yes if monthly investment > 0
    answers["investment_diversification"] = "yes" if user_data.get("investment", 0) > 0 else "no"

    # Debt health: EMI < 30% of income
    emi_ratio = (user_data.get("emi", 0) / user_data.get("income", 1)) if user_data.get("income", 0) > 0 else 1
    answers["debt_health"] = "yes" if emi_ratio < 0.3 else "no"

    # Tax efficiency: yes if tax_status is not "none"
    answers["tax_efficiency"] = "yes" if user_data.get("tax_status", "none") != "none" else "no"

    # Retirement readiness: yes if monthly investment > 0 (simplified)
    answers["retirement_readiness"] = "yes" if user_data.get("investment", 0) > 0 else "no"

    # Compute scores using your existing function
    scores = compute_money_health_score(answers)

    # Map to category scores and weights (as per your Streamlit UI)
    categoryScores = {
        "savings": min(int(months * 2), 20),  # up to 10+ months = 20/20
        "emergency": int(scores["emergency_preparedness"] * 20),
        "investment": int(scores["investment_diversification"] * 20),
        "debt": int(scores["debt_health"] * 15),
        "insurance": int(scores["insurance_coverage"] * 15),
        "tax": int(scores["tax_efficiency"] * 10),
    }
    totalScore = sum(categoryScores.values())

    return {
        "totalScore": totalScore,
        "categoryScores": categoryScores,
        "rawScores": scores,
        "answers": answers,
    }
