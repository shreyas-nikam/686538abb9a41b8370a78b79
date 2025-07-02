
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def calculate_put_call_parity(S, K, T, r, is_call):
    # Calculate the present value of the strike price
    PV_K = K * np.exp(-r * T)
    
    if is_call:
        # If we have the call price, calculate the put price
        C = S - PV_K
        P = C - S + PV_K
    else:
        # If we have the put price, calculate the call price
        P = PV_K - S
        C = P + S - PV_K
    
    return C, P

def run_page2():
    st.header("Put-Call Parity")

    st.markdown(r'''
    Put-Call Parity is a principle that defines the relationship between the price of European put options and European call options of the same class, that is, with the same underlying asset, strike price, and expiration date.

    The put-call parity formula is:

    $$S_0 + P = C + rac{K}{(1+r)^T}$$

    Where:
    - $S_0$ is the current price of the underlying asset
    - $P$ is the price of the European put option
    - $C$ is the price of the European call option
    - $K$ is the strike price of both options
    - $r$ is the risk-free interest rate
    - $T$ is the time to expiration

    This relationship must hold to prevent arbitrage opportunities in an efficient market.
    ''')

    # User inputs
    S = st.number_input("Current stock price (S)", min_value=1.0, value=100.0, step=1.0)
    K = st.number_input("Strike price (K)", min_value=1.0, value=100.0, step=1.0)
    T = st.number_input("Time to maturity (T) in years", min_value=0.1, value=1.0, step=0.1)
    r = st.number_input("Risk-free rate (r)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)
    option_type = st.radio("Select the option price you know", ('Call', 'Put'))
    option_price = st.number_input(f"Enter the {option_type} option price", min_value=0.0, value=10.0, step=0.1)

    is_call = option_type == 'Call'
    C, P = calculate_put_call_parity(S, K, T, r, is_call)

    st.subheader("Results")
    st.write(f"Call option price: ${C:.2f}")
    st.write(f"Put option price: ${P:.2f}")

    # Verify put-call parity
    left_side = S + P
    right_side = C + K * np.exp(-r * T)
    st.write(f"Left side of equation (S + P): ${left_side:.2f}")
    st.write(f"Right side of equation (C + K/(1+r)^T): ${right_side:.2f}")
    st.write(f"Difference: ${abs(left_side - right_side):.2f}")

    if abs(left_side - right_side) < 0.01:
        st.success("Put-Call Parity holds!")
    else:
        st.warning("There might be an arbitrage opportunity or an error in the inputs.")

    # Sensitivity analysis
    st.subheader("Sensitivity Analysis")
    st.write("See how the put-call parity relationship changes with different stock prices:")

    stock_prices = np.linspace(S * 0.5, S * 1.5, 100)
    call_prices = []
    put_prices = []

    for s in stock_prices:
        c, p = calculate_put_call_parity(s, K, T, r, True)
        call_prices.append(c)
        put_prices.append(p)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=stock_prices, y=call_prices, mode='lines', name='Call Price'))
    fig.add_trace(go.Scatter(x=stock_prices, y=put_prices, mode='lines', name='Put Price'))
    fig.update_layout(title='Option Prices vs Stock Price',
                      xaxis_title='Stock Price',
                      yaxis_title='Option Price')
    st.plotly_chart(fig)

    st.markdown('''
    This chart illustrates how call and put option prices change with the stock price, while keeping all other parameters constant. 
    Key observations:
    - As the stock price increases, the call option price increases and the put option price decreases.
    - The call and put lines are symmetrical, reflecting the put-call parity relationship.
    - At the point where the stock price equals the strike price (adjusted for the time value of money), the call and put prices are equal.
    ''')
