
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def calculate_put_call_parity(S, K, T, r, call_price=None, put_price=None):
    if call_price is not None:
        put_price = call_price - S + K * np.exp(-r * T)
        return put_price
    elif put_price is not None:
        call_price = put_price + S - K * np.exp(-r * T)
        return call_price
    else:
        return None

def run_put_call_parity():
    st.header("Put-Call Parity")
    
    st.markdown(r'''
    Put-Call Parity is a principle that defines the relationship between the price of European put options and European call options of the same class, that is, with the same underlying asset, strike price, and expiration date.

    The Put-Call Parity formula is:

    $$S_0 + P_0 = c_0 + \frac{X}{(1 + r)^T}$$

    Where:
    - $S_0$ is the current stock price
    - $P_0$ is the put option price
    - $c_0$ is the call option price
    - $X$ is the strike price
    - $r$ is the risk-free interest rate
    - $T$ is the time to expiration

    This relationship should hold to prevent arbitrage opportunities.
    ''')

    # User inputs
    S = st.number_input("Current stock price ($)", min_value=0.01, value=100.0, step=0.01)
    K = st.number_input("Strike price ($)", min_value=0.01, value=100.0, step=0.01)
    T = st.number_input("Time to expiration (years)", min_value=0.01, value=1.0, step=0.01)
    r = st.number_input("Risk-free rate (%)", min_value=0.0, value=5.0, step=0.1) / 100

    option_type = st.radio("Select the option price you want to calculate:", ('Put', 'Call'))

    if option_type == 'Put':
        call_price = st.number_input("Call option price ($)", min_value=0.01, value=10.0, step=0.01)
        if st.button("Calculate Put Price"):
            put_price = calculate_put_call_parity(S, K, T, r, call_price=call_price)
            st.success(f"The put option price is: ${put_price:.2f}")

            # Visualization
            call_prices = np.linspace(0, call_price * 2, 100)
            put_prices = [calculate_put_call_parity(S, K, T, r, call_price=cp) for cp in call_prices]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=call_prices, y=put_prices, mode='lines', name='Put-Call Parity'))
            fig.add_trace(go.Scatter(x=[call_price], y=[put_price], mode='markers', name='Current Prices'))
            fig.update_layout(title='Put-Call Parity Relationship',
                              xaxis_title='Call Option Price ($)',
                              yaxis_title='Put Option Price ($)')
            st.plotly_chart(fig)

    else:  # Call
        put_price = st.number_input("Put option price ($)", min_value=0.01, value=10.0, step=0.01)
        if st.button("Calculate Call Price"):
            call_price = calculate_put_call_parity(S, K, T, r, put_price=put_price)
            st.success(f"The call option price is: ${call_price:.2f}")

            # Visualization
            put_prices = np.linspace(0, put_price * 2, 100)
            call_prices = [calculate_put_call_parity(S, K, T, r, put_price=pp) for pp in put_prices]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=put_prices, y=call_prices, mode='lines', name='Put-Call Parity'))
            fig.add_trace(go.Scatter(x=[put_price], y=[call_price], mode='markers', name='Current Prices'))
            fig.update_layout(title='Put-Call Parity Relationship',
                              xaxis_title='Put Option Price ($)',
                              yaxis_title='Call Option Price ($)')
            st.plotly_chart(fig)

    st.markdown('''
    The graph above illustrates the Put-Call Parity relationship. 
    The line represents all possible combinations of put and call prices that satisfy the Put-Call Parity equation. 
    The point represents the current prices of the put and call options.
    ''')

if __name__ == "__main__":
    run_put_call_parity()
