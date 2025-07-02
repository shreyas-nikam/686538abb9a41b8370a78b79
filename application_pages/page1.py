
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def run_page1():
    st.title("Overview of Derivative Pricing")

    st.markdown("""
    ## Understanding Derivative Valuation

    Derivative valuation is a critical aspect of financial engineering. Derivatives, such as options and futures, derive their value from an underlying asset. The most common methods for valuing derivatives involve calculating the expected payoff at a future date and discounting it back to the present.

    ### Core Concepts

    1.  **Risk-Neutral Valuation**: Assumes that investors are indifferent to risk and only require a return equal to the risk-free rate.
    2.  **Discounted Cash Flows (DCF)**: Determines the present value of expected future cash flows.

    ### Formulas and Explanations

    #### Present Value Formula
    The present value (\(PV\)) of a future cash flow is calculated as:

    $$
    PV = \frac{CF}{(1 + r)^t}
    $$

    Where:
    *   \(CF\) is the future cash flow,
    *   \(r\) is the discount rate (risk-free rate),
    *   \(t\) is the time to maturity.

    #### Expected Payoff
    The expected payoff is the weighted average of potential payoffs, using risk-neutral probabilities:

    $$
    \mathbb{E}[\text{Payoff}] = \sum_{i=1}^{n} p_i \cdot \text{Payoff}_i
    $$

    Where:
    *   \(p_i\) is the risk-neutral probability of outcome \(i\),
    *   \(\text{Payoff}_i\) is the payoff for outcome \(i\).

    ### Interactive Example

    Let's consider a simple example: a derivative that pays \$100 if a stock price exceeds a certain level in one year. We assume a risk-free rate of 5%.
    """)

    # Input parameters
    probability = st.slider("Probability of exceeding level:", 0.0, 1.0, 0.5)
    risk_free_rate = st.slider("Risk-free rate:", 0.0, 0.1, 0.05)

    # Calculate expected payoff
    expected_payoff = probability * 100

    # Calculate present value
    present_value = expected_payoff / (1 + risk_free_rate)

    st.write(f"Expected Payoff: ${expected_payoff:.2f}")
    st.write(f"Present Value: ${present_value:.2f}")

    # Visualization
    data = {'Scenario': ['Expected Payoff', 'Present Value'],
            'Value': [expected_payoff, present_value]}
    df = pd.DataFrame(data)

    fig = px.bar(df, x='Scenario', y='Value', title='Expected Payoff vs Present Value')
    st.plotly_chart(fig)
