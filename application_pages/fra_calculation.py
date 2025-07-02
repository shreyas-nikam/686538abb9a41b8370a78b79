
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def calculate_fra_settlement(N, R_K, R_F, d):
    return N * (R_K - R_F) * (d / 360) / (1 + R_K * (d / 360))

def run_fra_calculation():
    st.header("Forward Rate Agreement (FRA) Calculation")
    
    st.markdown(open("application_pages/fra_calculation.md", "r").read())
    
    col1, col2 = st.columns(2)

    with col1:
        N = st.number_input("Notional principal (N)", min_value=1000.0, value=1000000.0, step=1000.0)
        R_K = st.number_input("Observed interest rate (R_K)", min_value=0.01, value=0.05, step=0.01, format="%.2f")
        R_F = st.number_input("FRA rate (R_F)", min_value=0.01, value=0.04, step=0.01, format="%.2f")
        d = st.number_input("Number of days", min_value=1, value=180, step=1)

    if st.button("Calculate FRA Settlement"):
        settlement = calculate_fra_settlement(N, R_K, R_F, d)
        st.success(f"The FRA settlement amount is: ${settlement:.2f}")

        with col2:
            observed_rates = np.linspace(R_F - 0.02, R_F + 0.02, 100)
            settlements = [calculate_fra_settlement(N, r, R_F, d) for r in observed_rates]

            fig = go.Figure(data=go.Scatter(x=observed_rates, y=settlements, mode='lines'))
            fig.update_layout(title='FRA Settlement vs Observed Rate', xaxis_title='Observed Rate', yaxis_title='Settlement Amount')
            st.plotly_chart(fig)

    st.markdown("The graph shows how the FRA settlement amount changes with different observed rates.")
