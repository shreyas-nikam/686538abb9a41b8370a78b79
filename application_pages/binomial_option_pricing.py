
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def binomial_option_price(S, K, T, r, sigma, N, option_type='call'):
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    
    ST = S * (u ** np.arange(N, -1, -1)) * (d ** np.arange(0, N+1))
    
    if option_type == 'call':
        C = np.maximum(ST - K, 0)
    else:
        C = np.maximum(K - ST, 0)
    
    for i in range(N-1, -1, -1):
        C = np.exp(-r * dt) * (p * C[:-1] + (1-p) * C[1:])
    
    return C[0]

def run_binomial_option_pricing():
    st.header("Binomial Option Pricing Model")
    
    st.markdown(open("application_pages/binomial_option_pricing.md", "r").read())
    
    col1, col2 = st.columns(2)

    with col1:
        S = st.number_input("Current stock price (S)", min_value=1.0, value=100.0, step=1.0)
        K = st.number_input("Strike price (K)", min_value=1.0, value=100.0, step=1.0)
        T = st.number_input("Time to maturity (T) in years", min_value=0.1, value=1.0, step=0.1)
        r = st.number_input("Risk-free rate (r)", min_value=0.01, value=0.05, step=0.01, format="%.2f")
        sigma = st.number_input("Volatility (σ)", min_value=0.01, value=0.2, step=0.01, format="%.2f")
        N = st.number_input("Number of time steps", min_value=1, value=50, step=1)
        option_type = st.selectbox("Option type", ["call", "put"])

    if st.button("Calculate Option Price"):
        price = binomial_option_price(S, K, T, r, sigma, N, option_type)
        st.success(f"The {option_type} option price is: ${price:.2f}")

        with col2:
            stock_prices = np.linspace(S * 0.5, S * 1.5, 100)
            option_prices = [binomial_option_price(s, K, T, r, sigma, N, option_type) for s in stock_prices]

            fig = go.Figure(data=go.Scatter(x=stock_prices, y=option_prices, mode='lines'))
            fig.update_layout(title='Option Price vs Stock Price', xaxis_title='Stock Price', yaxis_title='Option Price')
            st.plotly_chart(fig)

    st.markdown("The graph shows how the option price changes with the underlying stock price.")
