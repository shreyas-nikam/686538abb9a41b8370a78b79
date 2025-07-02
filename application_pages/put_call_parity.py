
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def calculate_put_call_parity(S, K, T, r, call_price):
    put_price = call_price + K * np.exp(-r * T) - S
    return put_price

def run_put_call_parity():
    st.header("Put-Call Parity")
    
    st.markdown(r'''
    Put-Call Parity is a principle that defines the relationship between the price of European put options and European call options of the same class, that is, with the same underlying asset, strike price, and expiration date.

    The Put-Call Parity formula is:

    $$S_0 + P_0 = c_0 + \frac{X}{(1 + r)^T}$$

    Where:
    - $S_0$ is the current price of the underlying asset
    - $P_0$ is the current price of the European put option
    - $c_0$ is the current price of the European call option
    - $X$ is the strike price of the options
    - $r$ is the risk-free interest rate
    - $T$ is the time to expiration

    This relationship must hold to prevent arbitrage opportunities.
    ''')

    # User inputs
    S = st.number_input("Current stock price", min_value=1.0, value=100.0)
    K = st.number_input("Strike price", min_value=1.0, value=100.0)
    T = st.number_input("Time to maturity (in years)", min_value=0.1, value=1.0)
    r = st.number_input("Risk-free rate", min_value=0.0, max_value=1.0, value=0.05)
    call_price = st.number_input("Call option price", min_value=0.0, value=10.0)

    if st.button("Calculate Put Price"):
        put_price = calculate_put_call_parity(S, K, T, r, call_price)
        st.success(f"The put option price according to put-call parity is: ${put_price:.2f}")

        # Visualization
        call_prices = np.linspace(0, 20, 100)
        put_prices = [calculate_put_call_parity(S, K, T, r, c) for c in call_prices]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=call_prices, y=put_prices, mode='lines', name='Put-Call Parity'))
        fig.update_layout(title='Put-Call Parity Relationship',
                          xaxis_title='Call Option Price',
                          yaxis_title='Put Option Price')
        st.plotly_chart(fig)

        st.markdown('''
        The graph above illustrates the linear relationship between call and put option prices 
        as defined by put-call parity. For a given set of parameters (stock price, strike price, 
        time to maturity, and risk-free rate), as the call option price increases, the corresponding 
        put option price decreases linearly to maintain the parity relationship.
        ''')

if __name__ == "__main__":
    run_put_call_parity()
