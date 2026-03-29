# ===============================
# FIX IMPORT PATH ISSUE
# ===============================
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# ===============================
# IMPORT LIBRARIES
# ===============================
import streamlit as st
import plotly.graph_objects as go

# ===============================
# IMPORT YOUR MODULES
# ===============================
from utils.score_calculator import calculate_money_health_score
from utils.insight_engine import generate_insights
from utils.recommendation_engine import generate_recommendations

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(page_title="AI Money Mentor", layout="wide")

st.title("💰 AI Money Mentor")
st.subheader("📊 Money Health Score Dashboard")

# ===============================
# USER INPUT
# ===============================
st.sidebar.header("Enter Your Financial Details")

income = st.sidebar.number_input("Monthly Income (₹)", min_value=0, value=50000)
expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=0, value=30000)
savings = st.sidebar.number_input("Total Savings (₹)", min_value=0, value=100000)
investment = st.sidebar.number_input("Monthly Investment (₹)", min_value=0, value=10000)
emi = st.sidebar.number_input("Monthly EMI (₹)", min_value=0, value=5000)

insurance = st.sidebar.selectbox(
    "Insurance Coverage",
    ["None", "Health", "Term", "Health + Term"]
)

tax_utilization = st.sidebar.selectbox(
    "Tax Utilization",
    ["None", "Partial", "Full"]
)

# ===============================
# PROCESS DATA
# ===============================
if st.sidebar.button("Calculate Score"):

    user_data = {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "investment": investment,
        "emi": emi,
        "insurance": insurance,
        "tax_utilization": tax_utilization
    }

    # Calculate score
    result = calculate_money_health_score(user_data)

    total_score = result["totalScore"]
    category_scores = result["categoryScores"]

    # Generate insights & recommendations
    insights = generate_insights(result)
    recommendations = generate_recommendations(result)

    # ===============================
    # SCORE DISPLAY
    # ===============================
    st.markdown("## 🎯 Your Money Health Score")

    # Color logic
    if total_score < 50:
        color = "red"
    elif total_score < 75:
        color = "orange"
    else:
        color = "green"

    st.markdown(
        f"<h1 style='text-align: center; color: {color};'>{total_score}/100</h1>",
        unsafe_allow_html=True
    )

    # ===============================
    # CATEGORY BREAKDOWN (BAR CHART)
    # ===============================
    st.markdown("## 📊 Category Breakdown")

    fig = go.Figure(go.Bar(
        x=list(category_scores.keys()),
        y=list(category_scores.values())
    ))

    fig.update_layout(
        xaxis_title="Categories",
        yaxis_title="Score",
        yaxis=dict(range=[0, 20])
    )

    st.plotly_chart(fig, use_container_width=True)

    # ===============================
    # INSIGHTS
    # ===============================
    st.markdown("## 🔍 Insights")

    for insight in insights:
        st.write(f"• {insight}")

    # ===============================
    # RECOMMENDATIONS
    # ===============================
    st.markdown("## 💡 Recommendations")

    for rec in recommendations:
        st.write(f"• {rec}")

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.markdown(
    "👉 *Money Health Score simplifies personal finance into a single number — and tells you exactly how to improve it.*"
)