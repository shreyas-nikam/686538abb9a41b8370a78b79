
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def calculate_put_call_parity(S, K, T, r, c):
    p = c + K * np.exp(-r * T) - S
    return p

def run_put_call_parity():
    st.header("Put-Call Parity")
    
    st.markdown(r'''
    Put-Call Parity is a principle that defines the relationship between the price of European put options and European call options of the same class, that is, with the same underlying asset, strike price, and expiration date.
    
    The put-call parity formula is:
    
    $$S_0 + P_0 = c_0 + rac{X}{(1 + r)^T}$$
    
    Where:
    - $S_0$ is the current price of the underlying asset
    - $P_0$ is the current price of the European put option
    - $c_0$ is the current price of the European call option
    - $X$ is the strike price of the options
    - $r$ is the risk-free interest rate
    - $T$ is the time to expiration
    ''')

    col1, col2 = st.columns(2)

    with col1:
        S = st.number_input("Current stock price (S)", min_value=1.0, value=100.0, step=1.0)
        K = st.number_input("Strike price (K)", min_value=1.0, value=100.0, step=1.0)
        T = st.number_input("Time to maturity (T) in years", min_value=0.1, value=1.0, step=0.1)

    with col2:
        r = st.number_input("Risk-free rate (r)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)
        c = st.number_input("Call option price (c)", min_value=0.0, value=10.0, step=0.1)

    if st.button("Calculate Put Price"):
        p = calculate_put_call_parity(S, K, T, r, c)
        st.success(f"The put option price according to put-call parity is: ${p:.2f}")

        # Create a range of stock prices for visualization
        stock_prices = np.linspace(S * 0.5, S * 1.5, 100)
        call_prices = [max(s - K, 0) for s in stock_prices]
        put_prices = [max(K - s, 0) for s in stock_prices]

        # Plot the option payoffs
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=stock_prices, y=call_prices, mode='lines', name='Call Option Payoff'))
        fig.add_trace(go.Scatter(x=stock_prices, y=put_prices, mode='lines', name='Put Option Payoff'))
        fig.update_layout(title='Call and Put Option Payoffs at Expiration',
                          xaxis_title='Stock Price',
                          yaxis_title='Option Payoff')
        st.plotly_chart(fig)

        st.markdown('''
        ### Interpretation
        
        The graph above shows the payoffs for call and put options at expiration:
        
        - The call option (blue line) increases in value as the stock price increases above the strike price.
        - The put option (orange line) increases in value as the stock price decreases below the strike price.
        
        Put-call parity ensures that these two options, along with the underlying stock and a risk-free bond, maintain a specific relationship to prevent arbitrage opportunities.
        ''')

if __name__ == "__main__":
    run_put_call_parity()
