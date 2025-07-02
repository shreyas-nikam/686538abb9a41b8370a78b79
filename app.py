
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

1. Binomial Option Pricing Model
2. Put-Call Parity
3. Forward Price Formula
4. Forward Rate Agreement (FRA)

These models are essential for understanding and valuing financial derivatives. Let's break down each concept:

### Binomial Option Pricing Model

The binomial option pricing model calculates the theoretical value for options using a binomial tree. The model uses the following formula:

$$C_0 = rac{\pi C_u + (1 - \pi) C_d}{1 + r}$$

Where:
- $C_0$: Call option price at time 0
- $C_u$: Call option price if the underlying asset price goes up
- $C_d$: Call option price if the underlying asset price goes down
- $\pi$: Risk-neutral probability of an upward move
- $r$: Risk-free interest rate

The risk-neutral probability is calculated as:

$$\pi = rac{1 + r - d}{u - d}$$

Where:
- $u$: Up factor
- $d$: Down factor

### Put-Call Parity

Put-Call Parity establishes a relationship between European put and call options:

$$S_0 + P_0 = c_0 + rac{X}{(1 + r)^T}$$

Where:
- $S_0$: Current price of the underlying asset
- $P_0$: Current price of the European put option
- $c_0$: Current price of the European call option
- $X$: Strike price of the options
- $r$: Risk-free interest rate
- $T$: Time to expiration

### Forward Price Formula

The forward price formula determines the price today at which an asset can be bought at a future date:

$$F_0 = S_0(1 + r)^T$$

Where:
- $F_0$: Forward price
- $S_0$: Current spot price
- $r$: Risk-free rate
- $T$: Time until expiration

### Forward Rate Agreement (FRA)

A forward rate agreement ensures a specific rate for a future deposit:

$$	ext{Settlement at maturity} = N \times \frac{(R_K - R_F) \times \frac{d}{360}}{1 + R_K \frac{d}{360}}$$

Where:
- $N$: The notional principal
- $R_k$: The interest rate for the term the FRA is trying to cover
- $R_F$: The rate in the FRA agreement to be paid
- $d$: Number of days

Explore these concepts using the interactive tools provided in this lab!
''')

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Binomial Option Pricing", "Put-Call Parity", "Forward Price", "Forward Rate Agreement"])

if page == "Binomial Option Pricing":
    from application_pages.binomial_option_pricing import run_binomial_option_pricing
    run_binomial_option_pricing()
elif page == "Put-Call Parity":
    from application_pages.put_call_parity import run_put_call_parity
elif page == "Forward Price":
    from application_pages.forward_price import run_forward_price
elif page == "Forward Rate Agreement":
    from application_pages.forward_rate_agreement import run_forward_rate_agreement
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
