
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def calculate_binomial_option_price(S, K, T, r, sigma, N, option_type='call'):
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    
    # Initialize asset prices at maturity
    ST = S * (u ** np.arange(N, -1, -1)) * (d ** np.arange(0, N + 1))
    
    # Initialize option values at maturity
    if option_type == 'call':
        C = np.maximum(ST - K, 0)
    else:  # put
        C = np.maximum(K - ST, 0)
    
    # Backward iteration
    for i in range(N - 1, -1, -1):
        C = np.exp(-r * dt) * (p * C[:-1] + (1 - p) * C[1:])
    
    return C[0]

def run_binomial_option_pricing():
    st.header("Binomial Option Pricing Model")
    
    st.markdown(r'''
    The Binomial Option Pricing Model is a numerical method used to value options. It works by constructing a binomial tree that represents different possible paths that might be followed by the stock price over the life of the option.

    The model calculates the option price at each node of the tree, working backwards from the expiration to the present. The formula for the option price at each node is:

    $$C_0 = \frac{\pi C_u + (1 - \pi) C_d}{1 + r}$$

    Where:
    - $C_0$ is the current option price
    - $C_u$ is the option price if the stock price goes up
    - $C_d$ is the option price if the stock price goes down
    - $\pi$ is the risk-neutral probability
    - $r$ is the risk-free interest rate
    ''')

    # User inputs
    S = st.number_input("Current stock price ($)", min_value=0.01, value=100.0, step=0.01)
    K = st.number_input("Strike price ($)", min_value=0.01, value=100.0, step=0.01)
    T = st.number_input("Time to expiration (years)", min_value=0.01, value=1.0, step=0.01)
    r = st.number_input("Risk-free rate (%)", min_value=0.0, value=5.0, step=0.1) / 100
    sigma = st.number_input("Volatility (%)", min_value=0.1, value=20.0, step=0.1) / 100
    N = st.number_input("Number of time steps", min_value=1, value=50, step=1)
    option_type = st.selectbox("Option type", ['call', 'put'])

    if st.button("Calculate Option Price"):
        price = calculate_binomial_option_price(S, K, T, r, sigma, N, option_type)
        st.success(f"The {option_type} option price is: ${price:.2f}")

        # Sensitivity analysis
        steps = 50
        stock_prices = np.linspace(S * 0.5, S * 1.5, steps)
        option_prices = [calculate_binomial_option_price(s, K, T, r, sigma, N, option_type) for s in stock_prices]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=stock_prices, y=option_prices, mode='lines', name='Option Price'))
        fig.update_layout(title='Option Price Sensitivity to Stock Price',
                          xaxis_title='Stock Price ($)',
                          yaxis_title='Option Price ($)')
        st.plotly_chart(fig)

        st.markdown('''
        The graph above shows how the option price changes with the underlying stock price. 
        This relationship is known as the option's delta and is a crucial concept in option pricing and risk management.
        ''')

if __name__ == "__main__":
    run_binomial_option_pricing()
