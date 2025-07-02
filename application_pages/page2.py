
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def calculate_simple_interest(principal, rate, time):
    return principal * (1 + rate * time)

def calculate_compound_interest(principal, rate, time, frequency):
    if frequency == "Annually":
        n = 1
    else:
        n = 12
    return principal * (1 + rate / n)**(n * time)

def run_page2():
    st.header("Compound Interest Visualizer")

    principal = st.number_input("Principal Amount", value=1000)
    annual_rate = st.number_input("Annual Interest Rate (%)", value=5.0) / 100
    investment_duration = st.number_input("Investment Duration (Years)", value=10)
    compounding_frequency = st.radio("Compounding Frequency", options=["Annually", "Monthly"])

    simple_interest_fv = calculate_simple_interest(principal, annual_rate, investment_duration)
    compound_interest_fv = calculate_compound_interest(principal, annual_rate, investment_duration, compounding_frequency)

    # Data Preparation
    time_periods = np.arange(1, int(investment_duration) + 1)
    simple_interest_values = [calculate_simple_interest(principal, annual_rate, t) for t in time_periods]
    compound_interest_values = [calculate_compound_interest(principal, annual_rate, t, compounding_frequency) for t in time_periods]

    df = pd.DataFrame({
        "Time": time_periods,
        "Simple Interest": simple_interest_values,
        "Compound Interest": compound_interest_values
    })

    # Interactive Chart
    fig = px.line(df, x="Time", y=["Simple Interest", "Compound Interest"], title='Simple vs Compound Interest')
    st.plotly_chart(fig)

    st.write("Future Value (Simple Interest):", simple_interest_fv)
    st.write("Future Value (Compound Interest):", compound_interest_fv)
    st.write("Compound interest earns interest on interest, leading to significant growth over time.")
    st.markdown("### Compound Interest Formula")
    st.latex(r"FV = P(1 + \frac{r}{n})^{nt}")

if __name__ == "__main__":
    run_page2()
