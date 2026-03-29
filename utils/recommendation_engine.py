"""
recommendation_engine.py: Generates actionable recommendations from Money Health Score.
"""

def generate_recommendations(result):
    recs = []

    category_scores = result.get("categoryScores", {})

    # ===============================
    # SAVINGS
    # ===============================
    if category_scores.get('savings', 0) < 10:
        recs.append("Reduce non-essential expenses and aim to save at least 20–30% of your income.")

    # ===============================
    # EMERGENCY FUND
    # ===============================
    if category_scores.get('emergency', 0) < 15:
        recs.append("Build an emergency fund covering 3–6 months of expenses for financial security.")

    # ===============================
    # INVESTMENTS
    # ===============================
    if category_scores.get('investment', 0) < 15:
        recs.append("Start or increase your SIP — consider investing an additional ₹5,000/month in diversified mutual funds.")

    # ===============================
    # DEBT
    # ===============================
    if category_scores.get('debt', 0) < 10:
        recs.append("Prioritize repaying high-interest loans to reduce your debt burden.")

    # ===============================
    # INSURANCE
    # ===============================
    if category_scores.get('insurance', 0) < 10:
        recs.append("Get adequate health and term insurance to protect against financial risks.")

    # ===============================
    # TAX
    # ===============================
    if category_scores.get('tax', 0) < 7:
        recs.append("Maximize tax savings using instruments like ELSS, PPF, and insurance under Sections 80C and 80D.")

    # ===============================
    # POSITIVE CASE
    # ===============================
    if not recs:
        recs.append("Your financial strategy is strong — continue maintaining this discipline and review periodically.")

    return recs