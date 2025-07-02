
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

def run_page1():
    st.header("Binomial Option Pricing Model")

    st.markdown(r'''
    The Binomial Option Pricing Model is a numerical method used to value options. It works by constructing a binomial tree that represents different possible paths that might be followed by the stock price over the life of the option.

    The model is based on a simple assumption about asset price movement: in each time step, the price will either move up by a factor $u$ or down by a factor $d$ with probabilities $p$ and $1-p$ respectively.

    The key formula for the option price is:

    $$C_0 = rac{\pi C_u + (1 - \pi) C_d}{1 + r}$$

    Where:
    - $C_0$ is the current option price
    - $C_u$ is the option value if the stock price goes up
    - $C_d$ is the option value if the stock price goes down
    - $\pi$ is the risk-neutral probability
    - $r$ is the risk-free interest rate

    This model allows us to value options by working backwards from the potential future stock prices to the present.
    ''')

    # User inputs
    S = st.number_input("Current stock price (S)", min_value=1.0, value=100.0, step=1.0)
    K = st.number_input("Strike price (K)", min_value=1.0, value=100.0, step=1.0)
    T = st.number_input("Time to maturity (T) in years", min_value=0.1, value=1.0, step=0.1)
    r = st.number_input("Risk-free rate (r)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)
    sigma = st.number_input("Volatility (sigma)", min_value=0.0, max_value=1.0, value=0.2, step=0.01)
    N = st.number_input("Number of time steps (N)", min_value=1, value=50, step=1)
    option_type = st.selectbox("Option type", ['call', 'put'])

    # Calculate option price
    option_price = calculate_binomial_option_price(S, K, T, r, sigma, N, option_type)

    st.write(f"The estimated {option_type} option price is: ${option_price:.2f}")

    # Sensitivity analysis
    st.subheader("Sensitivity Analysis")
    st.write("See how the option price changes with different parameters:")

    parameter = st.selectbox("Choose parameter to vary", ['S', 'K', 'T', 'r', 'sigma'])
    
    if parameter == 'S':
        range_values = np.linspace(S * 0.5, S * 1.5, 100)
        prices = [calculate_binomial_option_price(s, K, T, r, sigma, N, option_type) for s in range_values]
        x_label = "Stock Price"
    elif parameter == 'K':
        range_values = np.linspace(K * 0.5, K * 1.5, 100)
        prices = [calculate_binomial_option_price(S, k, T, r, sigma, N, option_type) for k in range_values]
        x_label = "Strike Price"
    elif parameter == 'T':
        range_values = np.linspace(T * 0.5, T * 1.5, 100)
        prices = [calculate_binomial_option_price(S, K, t, r, sigma, N, option_type) for t in range_values]
        x_label = "Time to Maturity"
    elif parameter == 'r':
        range_values = np.linspace(max(0, r - 0.05), min(1, r + 0.05), 100)
        prices = [calculate_binomial_option_price(S, K, T, rate, sigma, N, option_type) for rate in range_values]
        x_label = "Risk-free Rate"
    else:  # sigma
        range_values = np.linspace(max(0, sigma - 0.1), min(1, sigma + 0.1), 100)
        prices = [calculate_binomial_option_price(S, K, T, r, vol, N, option_type) for vol in range_values]
        x_label = "Volatility"

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=range_values, y=prices, mode='lines', name='Option Price'))
    fig.update_layout(title=f'{option_type.capitalize()} Option Price vs {x_label}',
                      xaxis_title=x_label,
                      yaxis_title='Option Price')
    st.plotly_chart(fig)

    st.markdown('''
    This sensitivity analysis shows how the option price changes as we vary one parameter while keeping all others constant. 
    This is crucial for understanding the option's behavior and for risk management.

    Key observations:
    - For call options, the price generally increases with stock price, time to maturity, risk-free rate, and volatility.
    - For put options, the price generally decreases with stock price and risk-free rate, but increases with time to maturity and volatility.
    - The relationship with the strike price is opposite for calls and puts: call prices decrease with strike price, while put prices increase.
    ''')
