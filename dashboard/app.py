import streamlit as st
import plotly.graph_objects as go
from utils.score_calculator import calculate_money_health_score
from utils.insight_engine import generate_insights
from utils.recommendation_engine import generate_recommendations

st.set_page_config(page_title="Money Health Score", layout="centered", page_icon="💰")
st.title("💰 Money Health Score - AI Money Mentor")

st.markdown("""
Enter your financial details below to get your Money Health Score, category breakdown, insights, and personalized recommendations.
""")

with st.form("user_input_form"):
    col1, col2 = st.columns(2)
    with col1:
        income = st.number_input("Monthly Income (₹)", min_value=0, value=50000, step=1000)
        expenses = st.number_input("Monthly Expenses (₹)", min_value=0, value=30000, step=1000)
        savings = st.number_input("Total Savings (₹)", min_value=0, value=100000, step=1000)
        investment = st.number_input("Monthly Investment (₹)", min_value=0, value=5000, step=500)
    with col2:
        emi = st.number_input("Total Monthly EMI (₹)", min_value=0, value=5000, step=500)
        health_insurance = st.checkbox("Health Insurance", value=True)
        term_insurance = st.checkbox("Term Insurance", value=False)
        tax_status = st.selectbox("Tax Saving Status", ["full", "partial", "none"], index=1)
    submitted = st.form_submit_button("Calculate Money Health Score")

if submitted:
    user_data = {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "investment": investment,
        "emi": emi,
        "health_insurance": health_insurance,
        "term_insurance": term_insurance,
        "tax_status": tax_status,
    }
    result = calculate_money_health_score(user_data)
    total_score = result["totalScore"]
    category_scores = result["categoryScores"]

    # Score color
    if total_score < 50:
        score_color = "red"
    elif total_score < 75:
        score_color = "orange"
    else:
        score_color = "green"

    st.markdown(f"## 🏆 Your Money Health Score: <span style='color:{score_color};font-size:48px'>{total_score}/100</span>", unsafe_allow_html=True)

    # Category breakdown bar chart
    st.markdown("### 📊 Category Breakdown")
    cat_names = ["Savings", "Emergency", "Investment", "Debt", "Insurance", "Tax"]
    cat_values = [category_scores[k] for k in ["savings", "emergency", "investment", "debt", "insurance", "tax"]]
    cat_weights = [20, 20, 20, 15, 15, 10]
    fig = go.Figure(go.Bar(
        x=cat_names,
        y=cat_values,
        marker_color=["#2ecc71" if v >= 15 else ("#f1c40f" if v >= 10 else "#e74c3c") for v in cat_values],
        text=[f"{v}/{w}" for v, w in zip(cat_values, cat_weights)],
        textposition="outside"
    ))
    fig.update_layout(yaxis=dict(range=[0, 20]), height=350, margin=dict(l=20, r=20, t=40, b=20))
    st.plotly_chart(fig, use_container_width=True)

    # Insights
    st.markdown("### 🔍 Insights")
    insights = generate_insights(category_scores)
    for ins in insights:
        st.info(ins)

    # Recommendations
    st.markdown("### 💡 Recommendations")
    recs = generate_recommendations(category_scores)
    for rec in recs:
        st.success(rec)
else:
    st.info("Fill the form and click 'Calculate Money Health Score' to begin.")
