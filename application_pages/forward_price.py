
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def calculate_forward_price(S, r, T):
    return S * np.exp(r * T)

def run_forward_price():
    st.header("Forward Price Formula")
    
    st.markdown(r'''
    The Forward Price Formula is used to determine the price today at which an asset can be bought at a future date. It's a key concept in forward contracts and futures pricing.

    The Forward Price Formula is:

    $$F_0 = S_0(1 + r)^T$$

    or in continuous compounding:

    $$F_0 = S_0e^{rT}$$

    Where:
    - $F_0$ is the forward price
    - $S_0$ is the current spot price
    - $r$ is the risk-free rate
    - $T$ is the time until expiration

    This formula assumes no dividends or carrying costs.
    ''')

    # User inputs
    S = st.number_input("Current spot price", min_value=1.0, value=100.0)
    r = st.number_input("Risk-free rate", min_value=0.0, max_value=1.0, value=0.05)
    T = st.number_input("Time to expiration (in years)", min_value=0.1, value=1.0)

    if st.button("Calculate Forward Price"):
        forward_price = calculate_forward_price(S, r, T)
        st.success(f"The forward price is: ${forward_price:.2f}")

        # Visualization
        times = np.linspace(0, 2, 100)
        prices = [calculate_forward_price(S, r, t) for t in times]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=times, y=prices, mode='lines', name='Forward Price'))
        fig.update_layout(title='Forward Price over Time',
                          xaxis_title='Time to Expiration (years)',
                          yaxis_title='Forward Price')
        st.plotly_chart(fig)

        st.markdown('''
        The graph above shows how the forward price changes with time to expiration. 
        As the time to expiration increases, the forward price increases exponentially. 
        This reflects the time value of money: the longer you wait to receive the asset, 
        the more you need to be compensated for the delay.
        ''')

if __name__ == "__main__":
    run_forward_price()
