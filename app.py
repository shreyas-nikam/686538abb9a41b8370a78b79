
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from application_pages.binomial_option_pricing import run_binomial_option_pricing
from application_pages.put_call_parity import run_put_call_parity
from application_pages.forward_price import run_forward_price
from application_pages.forward_rate_agreement import run_forward_rate_agreement

st.set_page_config(page_title="QuLab: Derivative Price Valuation", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: Derivative Price Valuation")
st.divider()

st.markdown(r'''
In this lab, we explore various derivative pricing models and concepts. The application allows users to interact with key financial models, adjust parameters, and visualize the results in real-time. The main concepts covered are:

1. **Binomial Option Pricing Model**: A method for valuing options using a discrete-time model of the varying price over time of the financial instrument underlying the option.

2. **Put-Call Parity**: A principle that defines the relationship between the price of European put options and European call options of the same class, that is, with the same underlying asset, strike price, and expiration date.

3. **Forward Price Formula**: A model used to determine the price today at which an asset can be bought at a future date.

4. **Forward Rate Agreement (FRA)**: A contract that ensures a specific rate is guaranteed for a future deposit.

Each of these concepts is explored in detail in their respective pages. You can navigate between them using the sidebar.

This interactive application allows you to:
- Upload synthetic datasets
- Adjust key parameters
- Visualize the impact of parameter changes on derivative values
- Understand the underlying mathematical concepts through interactive examples

Let's dive in and explore the world of derivative pricing!
''')

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Binomial Option Pricing", "Put-Call Parity", "Forward Price", "Forward Rate Agreement"])

if page == "Binomial Option Pricing":
    run_binomial_option_pricing()
elif page == "Put-Call Parity":
    run_put_call_parity()
elif page == "Forward Price":
    run_forward_price()
elif page == "Forward Rate Agreement":
    run_forward_rate_agreement()
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
