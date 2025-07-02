
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def calculate_put_call_parity(S, X, r, T, option_type):
    discount_factor = np.exp(-r * T)
    if option_type == 'call':
        return S - X * discount_factor
    else:
        return X * discount_factor - S

def run_put_call_parity():
    st.header("Put-Call Parity")
    
    st.markdown(open("application_pages/put_call_parity.md", "r").read())
    
    col1, col2 = st.columns(2)

    with col1:
        S = st.number_input("Current stock price (S)", min_value=1.0, value=100.0, step=1.0)
        X = st.number_input("Strike price (X)", min_value=1.0, value=100.0, step=1.0)
        r = st.number_input("Risk-free rate (r)", min_value=0.01, value=0.05, step=0.01, format="%.2f")
        T = st.number_input("Time to expiration (T) in years", min_value=0.1, value=1.0, step=0.1)
        option_value = st.number_input("Option value", min_value=0.0, value=10.0, step=0.1)
        option_type = st.selectbox("Option type", ["call", "put"])

    if st.button("Calculate Put-Call Parity"):
        parity_value = calculate_put_call_parity(S, X, r, T, option_type)
        
        if option_type == 'call':
            put_value = option_value - parity_value
            st.success(f"The corresponding put option value is: ${put_value:.2f}")
        else:
            call_value = option_value + parity_value
            st.success(f"The corresponding call option value is: ${call_value:.2f}")

        with col2:
            stock_prices = np.linspace(S * 0.5, S * 1.5, 100)
            call_values = [calculate_put_call_parity(s, X, r, T, 'call') + option_value for s in stock_prices]
            put_values = [calculate_put_call_parity(s, X, r, T, 'put') + option_value for s in stock_prices]

            fig = go.Figure()
            fig.add_trace(go.Scatter(x=stock_prices, y=call_values, mode='lines', name='Call Option'))
            fig.add_trace(go.Scatter(x=stock_prices, y=put_values, mode='lines', name='Put Option'))
            fig.update_layout(title='Put-Call Parity', xaxis_title='Stock Price', yaxis_title='Option Value')
            st.plotly_chart(fig)

    st.markdown("The graph shows how call and put option values change with the underlying stock price.")
