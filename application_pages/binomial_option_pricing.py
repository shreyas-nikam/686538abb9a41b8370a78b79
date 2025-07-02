
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def calculate_binomial_option_price(S, K, T, r, sigma, N, option_type='call'):
    # Calculate parameters
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
    
    # Backward induction
    for i in range(N - 1, -1, -1):
        C = np.exp(-r * dt) * (p * C[:-1] + (1 - p) * C[1:])
    
    return C[0]

def run_binomial_option_pricing():
    st.header("Binomial Option Pricing Model")
    
    st.markdown(r'''
    The Binomial Option Pricing Model is a numerical method used to value options. It works by constructing a binomial tree that represents different possible paths that might be followed by the stock price over the life of the option.

    The model is based on the following formula:

    $$C_0 = \frac{\pi C_u + (1 - \pi) C_d}{1 + r}$$

    Where:
    - $C_0$ is the current option price
    - $C_u$ is the option value if the stock price goes up
    - $C_d$ is the option value if the stock price goes down
    - $\pi$ is the risk-neutral probability
    - $r$ is the risk-free interest rate

    The risk-neutral probability $\pi$ is calculated as:

    $$\pi = \frac{1 + r - d}{u - d}$$

    Where $u$ and $d$ are the up and down factors for the stock price movement.
    ''')

    # User inputs
    S = st.number_input("Current stock price", min_value=1.0, value=100.0)
    K = st.number_input("Strike price", min_value=1.0, value=100.0)
    T = st.number_input("Time to maturity (in years)", min_value=0.1, value=1.0)
    r = st.number_input("Risk-free rate", min_value=0.0, max_value=1.0, value=0.05)
    sigma = st.number_input("Volatility", min_value=0.0, max_value=1.0, value=0.2)
    N = st.number_input("Number of time steps", min_value=1, value=100)
    option_type = st.selectbox("Option type", ['call', 'put'])

    if st.button("Calculate Option Price"):
        option_price = calculate_binomial_option_price(S, K, T, r, sigma, N, option_type)
        st.success(f"The {option_type} option price is: ${option_price:.2f}")

        # Sensitivity analysis
        sigmas = np.linspace(0.1, 0.5, 50)
        prices = [calculate_binomial_option_price(S, K, T, r, sig, N, option_type) for sig in sigmas]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=sigmas, y=prices, mode='lines', name='Option Price'))
        fig.update_layout(title='Option Price Sensitivity to Volatility',
                          xaxis_title='Volatility',
                          yaxis_title='Option Price')
        st.plotly_chart(fig)

        st.markdown('''
        The graph above shows how the option price changes with volatility. 
        As volatility increases, the option price typically increases because there's a higher chance 
        of the option ending up in-the-money.
        ''')

if __name__ == "__main__":
    run_binomial_option_pricing()
