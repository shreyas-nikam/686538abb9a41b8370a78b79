
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def calculate_forward_price(S, r, T):
    return S * (1 + r)**T

def run_forward_pricing():
    st.header("Forward Pricing")
    
    st.markdown(r'''
    The Forward Price Formula determines the price agreed today for a future transaction of an asset. It takes into account the current spot price, risk-free rate, and time to maturity.
    
    The formula for the forward price is:
    
    $$F_0 = S_0(1 + r)^T$$
    
    Where:
    - $F_0$ is the forward price
    - $S_0$ is the current spot price
    - $r$ is the risk-free rate
    - $T$ is the time until expiration (in years)
    ''')

    col1, col2 = st.columns(2)

    with col1:
        S = st.number_input("Current spot price (S)", min_value=1.0, value=100.0, step=1.0)
        r = st.number_input("Risk-free rate (r)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)

    with col2:
        T = st.number_input("Time to maturity (T) in years", min_value=0.1, value=1.0, step=0.1)

    if st.button("Calculate Forward Price"):
        F = calculate_forward_price(S, r, T)
        st.success(f"The forward price is: ${F:.2f}")

        # Create a range of spot prices for visualization
        spot_prices = np.linspace(S * 0.5, S * 1.5, 100)
        forward_prices = [calculate_forward_price(s, r, T) for s in spot_prices]

        # Plot the forward prices
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=spot_prices, y=forward_prices, mode='lines', name='Forward Price'))
        fig.add_trace(go.Scatter(x=spot_prices, y=spot_prices, mode='lines', name='Spot Price', line=dict(dash='dash')))
        fig.update_layout(title='Forward Price vs Spot Price',
                          xaxis_title='Spot Price',
                          yaxis_title='Price')
        st.plotly_chart(fig)

        st.markdown('''
        ### Interpretation
        
        The graph above shows how the forward price changes with the spot price:
        
        - The blue line represents the forward price for different spot prices.
        - The dashed line represents the spot price itself.
        
        As you can see, the forward price is always higher than the spot price due to the time value of money (represented by the risk-free rate). The difference between the forward price and spot price increases as the time to maturity increases or as the risk-free rate increases.
        ''')

if __name__ == "__main__":
    run_forward_pricing()
