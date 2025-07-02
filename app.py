
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(page_title="QuLab: Derivative Price Valuation", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Derivative Price Valuation")
st.divider()

st.markdown(r'''
In this lab, we explore various derivative pricing models and concepts, including:

1. **Binomial Option Pricing Model**: This model calculates the theoretical value of options using a binomial tree approach. The key formula for the call option price is:

   $$C_0 = rac{\pi C_u + (1 - \pi) C_d}{1 + r}$$

   Where $C_0$ is the call option price at time 0, $C_u$ and $C_d$ are the call option prices if the underlying asset price goes up or down, respectively, $\pi$ is the risk-neutral probability of an upward move, and $r$ is the risk-free interest rate.

2. **Put-Call Parity**: This principle establishes a relationship between European put and call options with the same strike price and expiration date:

   $$S_0 + P_0 = c_0 + rac{X}{(1 + r)^T}$$

   Where $S_0$ is the current price of the underlying asset, $P_0$ is the put option price, $c_0$ is the call option price, $X$ is the strike price, $r$ is the risk-free rate, and $T$ is the time to expiration.

3. **Forward Price Formula**: This formula determines the price today at which an asset can be bought at a future date:

   $$F_0 = S_0(1 + r)^T$$

   Where $F_0$ is the forward price, $S_0$ is the current spot price, $r$ is the risk-free rate, and $T$ is the time until expiration.

4. **Forward Rate Agreement (FRA)**: This contract ensures a specific rate is guaranteed for a future deposit:

   $$	ext{Settlement at maturity} = N 	imes rac{(R_K - R_F) 	imes rac{d}{360}}{1 + R_K rac{d}{360}}$$

   Where $N$ is the notional principal, $R_K$ is the interest rate for the term the FRA is trying to cover, $R_F$ is the rate in the FRA agreement to be paid, and $d$ is the number of days.

This lab provides an interactive platform to explore these concepts and visualize how changes in various parameters affect derivative prices.
''')

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Binomial Option Pricing", "Put-Call Parity", "Forward Pricing", "FRA Calculator"])

if page == "Binomial Option Pricing":
    from application_pages.binomial_option_pricing import run_binomial_option_pricing
    run_binomial_option_pricing()
elif page == "Put-Call Parity":
    from application_pages.put_call_parity import run_put_call_parity
    run_put_call_parity()
elif page == "Forward Pricing":
    from application_pages.forward_pricing import run_forward_pricing
    run_forward_pricing()
elif page == "FRA Calculator":
    from application_pages.fra_calculator import run_fra_calculator
    run_fra_calculator()
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
