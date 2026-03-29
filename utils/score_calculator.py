"""
score_calculator.py: Core logic for Money Health Score calculation.
"""

def calculate_savings_score(income, expenses):
    if income <= 0:
        return 0

    savings_rate = (income - expenses) / income

    if savings_rate >= 0.4:
        return 20
    elif savings_rate >= 0.25:
        return 15
    elif savings_rate >= 0.10:
        return 10
    elif savings_rate > 0:
        return 5
    return 0


def calculate_emergency_score(savings, expenses):
    if expenses <= 0:
        return 0

    months = savings / expenses

    if months >= 6:
        return 20
    elif months >= 3:
        return 15
    elif months >= 1:
        return 10
    elif months > 0:
        return 5
    return 0


def calculate_investment_score(investment, income):
    if income <= 0:
        return 0

    invest_pct = investment / income

    if invest_pct >= 0.3:
        return 20
    elif invest_pct >= 0.15:
        return 15
    elif invest_pct >= 0.05:
        return 10
    elif invest_pct > 0:
        return 5
    return 0


def calculate_debt_score(emi, income):
    if income <= 0:
        return 0

    ratio = emi / income

    if ratio < 0.2:
        return 15
    elif ratio <= 0.4:
        return 10
    else:
        return 5


def calculate_insurance_score(insurance):
    """
    insurance: string from UI
    """
    if insurance == "Health + Term":
        return 15
    elif insurance in ["Health", "Term"]:
        return 10
    return 5


def calculate_tax_score(tax_utilization):
    """
    tax_utilization: string from UI
    """
    tax_utilization = str(tax_utilization).lower()

    if tax_utilization == "full":
        return 10
    elif tax_utilization == "partial":
        return 7
    return 3


def calculate_money_health_score(user_data):
    # Safe extraction
    income = user_data.get('income', 0)
    expenses = user_data.get('expenses', 0)
    savings = user_data.get('savings', 0)
    investment = user_data.get('investment', 0)
    emi = user_data.get('emi', 0)
    insurance = user_data.get('insurance', "None")
    tax_utilization = user_data.get('tax_utilization', "None")

    scores = {}

    scores['savings'] = calculate_savings_score(income, expenses)
    scores['emergency'] = calculate_emergency_score(savings, expenses)
    scores['investment'] = calculate_investment_score(investment, income)
    scores['debt'] = calculate_debt_score(emi, income)
    scores['insurance'] = calculate_insurance_score(insurance)
    scores['tax'] = calculate_tax_score(tax_utilization)

    total = sum(scores.values())

    return {
        'totalScore': total,
        'categoryScores': scores
    }