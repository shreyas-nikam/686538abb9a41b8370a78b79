
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def calculate_forward_price(S, r, T):
    return S * (1 + r) ** T

def run_forward_pricing():
    st.header("Forward Pricing")
    
    st.markdown(r'''
    The Forward Price Formula is used to determine the price today at which an asset can be bought or sold for delivery at a future date. This is crucial in forward contracts and helps in understanding how current prices are determined for future transactions.

    The Forward Price Formula is:

    $$F_0 = S_0(1 + r)^T$$

    Where:
    - $F_0$ is the forward price
    - $S_0$ is the current spot price of the asset
    - $r$ is the risk-free interest rate
    - $T$ is the time until expiration (in years)

    This formula accounts for the time value of money, reflecting that the buyer of a forward contract doesn't need to pay until the delivery date.
    ''')

    # User inputs
    S = st.number_input("Current spot price ($)", min_value=0.01, value=100.0, step=0.01)
    r = st.number_input("Risk-free rate (%)", min_value=0.0, value=5.0, step=0.1) / 100
    T = st.number_input("Time to expiration (years)", min_value=0.01, value=1.0, step=0.01)

    if st.button("Calculate Forward Price"):
        forward_price = calculate_forward_price(S, r, T)
        st.success(f"The forward price is: ${forward_price:.2f}")

        # Visualization
        times = np.linspace(0, T * 2, 100)
        forward_prices = [calculate_forward_price(S, r, t) for t in times]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=times, y=forward_prices, mode='lines', name='Forward Price'))
        fig.add_trace(go.Scatter(x=[T], y=[forward_price], mode='markers', name='Current Forward Price'))
        fig.update_layout(title='Forward Price vs Time to Expiration',
                          xaxis_title='Time to Expiration (years)',
                          yaxis_title='Forward Price ($)')
        st.plotly_chart(fig)

        st.markdown('''
        The graph above shows how the forward price changes with the time to expiration. 
        As the time to expiration increases, the forward price typically increases due to the time value of money.
        ''')

if __name__ == "__main__":
    run_forward_pricing()
