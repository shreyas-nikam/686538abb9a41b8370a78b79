
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def binomial_option_price(S, K, T, r, sigma, N, option_type='call'):
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
    The Binomial Option Pricing Model calculates the theoretical value of an option using a discrete-time model of the varying price over time of the underlying financial instrument. 
    
    The key formula for the option price at each node is:
    
    $$C_0 = rac{\pi C_u + (1 - \pi) C_d}{1 + r}$$
    
    Where:
    - $C_0$ is the current option price
    - $C_u$ is the option price if the underlying goes up
    - $C_d$ is the option price if the underlying goes down
    - $\pi$ is the risk-neutral probability
    - $r$ is the risk-free rate
    ''')

    col1, col2 = st.columns(2)

    with col1:
        S = st.number_input("Current stock price (S)", min_value=1.0, value=100.0, step=1.0)
        K = st.number_input("Strike price (K)", min_value=1.0, value=100.0, step=1.0)
        T = st.number_input("Time to maturity (T) in years", min_value=0.1, value=1.0, step=0.1)
        r = st.number_input("Risk-free rate (r)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)

    with col2:
        sigma = st.number_input("Volatility (σ)", min_value=0.0, max_value=1.0, value=0.2, step=0.01)
        N = st.number_input("Number of time steps (N)", min_value=1, value=50, step=1)
        option_type = st.selectbox("Option type", ["call", "put"])

    if st.button("Calculate Option Price"):
        price = binomial_option_price(S, K, T, r, sigma, N, option_type)
        st.success(f"The {option_type} option price is: ${price:.2f}")

        # Create a range of stock prices for sensitivity analysis
        stock_prices = np.linspace(S * 0.5, S * 1.5, 100)
        option_prices = [binomial_option_price(s, K, T, r, sigma, N, option_type) for s in stock_prices]

        # Plot the option price sensitivity
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=stock_prices, y=option_prices, mode='lines', name='Option Price'))
        fig.update_layout(title='Option Price Sensitivity to Stock Price',
                          xaxis_title='Stock Price',
                          yaxis_title='Option Price')
        st.plotly_chart(fig)

        st.markdown('''
        ### Interpretation
        
        The graph above shows how the option price changes with the underlying stock price. 
        
        - For a call option, the price increases as the stock price increases.
        - For a put option, the price decreases as the stock price increases.
        
        The steepness of the curve indicates how sensitive the option price is to changes in the stock price, which is related to the option's delta.
        ''')

if __name__ == "__main__":
    run_binomial_option_pricing()
