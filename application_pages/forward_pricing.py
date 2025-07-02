
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def calculate_forward_price(S, r, T):
    return S * np.exp(r * T)

def run_forward_pricing():
    st.header("Forward Pricing")
    
    st.markdown(open("application_pages/forward_pricing.md", "r").read())
    
    col1, col2 = st.columns(2)

    with col1:
        S = st.number_input("Current spot price (S)", min_value=1.0, value=100.0, step=1.0)
        r = st.number_input("Risk-free rate (r)", min_value=0.01, value=0.05, step=0.01, format="%.2f")
        T = st.number_input("Time to expiration (T) in years", min_value=0.1, value=1.0, step=0.1)

    if st.button("Calculate Forward Price"):
        forward_price = calculate_forward_price(S, r, T)
        st.success(f"The forward price is: ${forward_price:.2f}")

        with col2:
            times = np.linspace(0, T * 2, 100)
            forward_prices = [calculate_forward_price(S, r, t) for t in times]

            fig = go.Figure(data=go.Scatter(x=times, y=forward_prices, mode='lines'))
            fig.update_layout(title='Forward Price over Time', xaxis_title='Time (years)', yaxis_title='Forward Price')
            st.plotly_chart(fig)

    st.markdown("The graph shows how the forward price changes over time.")
