"""
insight_engine.py: Generates insights based on Money Health Score categories.
"""

def generate_insights(result):
    insights = []

    category_scores = result.get("categoryScores", {})

    # ===============================
    # EMERGENCY FUND
    # ===============================
    if category_scores.get('emergency', 0) < 15:
        insights.append("Your emergency fund is below recommended levels (aim for 3–6 months of expenses).")

    # ===============================
    # SAVINGS
    # ===============================
    if category_scores.get('savings', 0) >= 15:
        insights.append("You have a strong savings discipline — great job!")

    elif category_scores.get('savings', 0) < 10:
        insights.append("Your savings rate is low — consider reducing discretionary expenses.")

    # ===============================
    # INVESTMENTS
    # ===============================
    if category_scores.get('investment', 0) < 15:
        insights.append("Your investment contribution is low — consider starting or increasing SIPs.")

    # ===============================
    # DEBT
    # ===============================
    if category_scores.get('debt', 0) < 10:
        insights.append("Your debt levels are high relative to income — this may impact long-term financial stability.")

    # ===============================
    # INSURANCE
    # ===============================
    if category_scores.get('insurance', 0) < 10:
        insights.append("You lack adequate insurance coverage — consider health and term insurance.")

    # ===============================
    # TAX
    # ===============================
    if category_scores.get('tax', 0) < 7:
        insights.append("You are not fully utilizing tax-saving options (80C, 80D, etc.).")

    # ===============================
    # POSITIVE SUMMARY
    # ===============================
    if not insights:
        insights.append("Your financial health is excellent — keep maintaining this discipline!")

    return insights