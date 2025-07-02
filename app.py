
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="QuLab: Derivative Price Valuation", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Derivative Price Valuation")
st.divider()

st.markdown('''
In this lab, we explore various derivative pricing models and concepts, including the Binomial Option Pricing Model, Put-Call Parity, Forward Price Formula, and Forward Rate Agreement (FRA). These models are essential for understanding and valuing financial derivatives.

1. **Binomial Option Pricing Model**: This model calculates the theoretical value of options using a discrete-time framework. It considers the possible up and down movements of the underlying asset price over time.

2. **Put-Call Parity**: This principle establishes a relationship between the prices of European put and call options with the same strike price and expiration date.

3. **Forward Price Formula**: This formula determines the price today at which an asset can be bought or sold for delivery at a future date.

4. **Forward Rate Agreement (FRA)**: This is a contract that guarantees a specific interest rate for a future deposit or loan.

Use the navigation menu on the left to explore each concept in detail and perform calculations with interactive inputs.
''')

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Binomial Option Pricing", "Put-Call Parity", "Forward Price", "Forward Rate Agreement"])

if page == "Binomial Option Pricing":
    from application_pages.binomial_option_pricing import run_binomial_option_pricing
    run_binomial_option_pricing()
elif page == "Put-Call Parity":
    from application_pages.put_call_parity import run_put_call_parity
    run_put_call_parity()
elif page == "Forward Price":
    from application_pages.forward_price import run_forward_price
    run_forward_price()
elif page == "Forward Rate Agreement":
    from application_pages.forward_rate_agreement import run_forward_rate_agreement
    run_forward_rate_agreement()
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
