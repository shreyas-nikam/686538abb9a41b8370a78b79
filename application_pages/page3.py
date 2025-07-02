
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def calculate_forward_price(S, r, T):
    return S * np.exp(r * T)

def calculate_fra_settlement(N, R_K, R_F, d):
    return N * (R_K - R_F) * (d / 360) / (1 + R_K * (d / 360))

def run_page3():
    st.header("Forward Contracts")

    st.markdown(r'''
    This page covers two types of forward contracts: Forward Price Formula and Forward Rate Agreement (FRA).

    ### Forward Price Formula

    The forward price formula determines the price today at which an asset can be bought at a future date:

    $$F_0 = S_0(1 + r)^T$$

    Where:
    - $F_0$ is the forward price
    - $S_0$ is the current spot price
    - $r$ is the risk-free rate
    - $T$ is the time until expiration

    ### Forward Rate Agreement (FRA)

    A Forward Rate Agreement (FRA) is a contract that ensures a specific rate is guaranteed for a future deposit:

    $$	ext{Settlement at maturity} = N 	imes rac{(R_K - R_F) 	imes rac{d}{360}}{1 + R_K rac{d}{360}}$$

    Where:
    - $N$ is the notional principal
    - $R_K$ is the interest rate for the term the FRA is trying to cover
    - $R_F$ is the rate in the FRA agreement to be paid
    - $d$ is the number of days
    ''')

    # Forward Price Formula
    st.subheader("Forward Price Formula")
    S = st.number_input("Current spot price (S)", min_value=1.0, value=100.0, step=1.0)
    r = st.number_input("Risk-free rate (r)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)
    T = st.number_input("Time to expiration (T) in years", min_value=0.1, value=1.0, step=0.1)

    forward_price = calculate_forward_price(S, r, T)
    st.write(f"The forward price is: ${forward_price:.2f}")

    # Sensitivity analysis for Forward Price
    st.write("Sensitivity Analysis: Forward Price vs Time to Expiration")
    T_range = np.linspace(0.1, 5, 100)
    forward_prices = [calculate_forward_price(S, r, t) for t in T_range]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=T_range, y=forward_prices, mode='lines', name='Forward Price'))
    fig.update_layout(title='Forward Price vs Time to Expiration',
                      xaxis_title='Time to Expiration (years)',
                      yaxis_title='Forward Price')
    st.plotly_chart(fig)

    # Forward Rate Agreement
    st.subheader("Forward Rate Agreement (FRA)")
    N = st.number_input("Notional principal (N)", min_value=1000.0, value=1000000.0, step=1000.0)
    R_K = st.number_input("Interest rate for the term (R_K)", min_value=0.0, max_value=1.0, value=0.06, step=0.01)
    R_F = st.number_input("Rate in FRA agreement (R_F)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)
    d = st.number_input("Number of days", min_value=1, value=180, step=1)

    fra_settlement = calculate_fra_settlement(N, R_K, R_F, d)
    st.write(f"The FRA settlement amount is: ${fra_settlement:.2f}")

    # Sensitivity analysis for FRA
    st.write("Sensitivity Analysis: FRA Settlement vs Interest Rate for the Term")
    R_K_range = np.linspace(max(0, R_K - 0.05), min(1, R_K + 0.05), 100)
    fra_settlements = [calculate_fra_settlement(N, r_k, R_F, d) for r_k in R_K_range]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=R_K_range, y=fra_settlements, mode='lines', name='FRA Settlement'))
    fig.update_layout(title='FRA Settlement vs Interest Rate for the Term',
                      xaxis_title='Interest Rate for the Term (R_K)',
                      yaxis_title='FRA Settlement')
    st.plotly_chart(fig)

    st.markdown('''
    These charts illustrate how the forward price and FRA settlement change with time to expiration and interest rate, respectively.
    Key observations:
    - The forward price increases exponentially with time to expiration, reflecting the time value of money.
    - The FRA settlement amount is positive when R_K > R_F (the actual rate is higher than the agreed rate) and negative when R_K < R_F.
    - The relationship between the FRA settlement and R_K is approximately linear for small changes in the rate.
    ''')
