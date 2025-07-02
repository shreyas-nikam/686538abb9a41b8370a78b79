
import streamlit as st

st.set_page_config(page_title="Derivative Price Valuation", layout="wide")
st.sidebar.image("https://images.unsplash.com/photo-1581090700227-9befdc9c7a49?ixlib=rb-4.0.1&auto=format&fit=crop&w=800&q=80")  # Placeholder image
st.sidebar.divider()
st.title("Derivative Price Valuation")
st.divider()

st.markdown(r"""
# Overview

In financial markets, derivatives are contracts whose value depends on the price of underlying assets, such as stocks, bonds, or commodities. Valuing derivatives accurately is crucial for risk management and trading strategies.

This application demonstrates how derivative prices are computed using models based on the **fundamental principle of discounting** future expected cash flows to the present value. The core idea is that the fair price of a derivative is the present value of expected payoffs under a risk-neutral measure, discounted at the appropriate risk-free rate.

The main formula used in derivative valuation is:

$$
V_0 = e^{-r T} \mathbb{E}^{\mathbb{Q}}[ 	ext{Payoff at } T ]
$$

where:
- \( V_0 \): current value of the derivative
- \( r \): risk-free interest rate
- \( T \): time to maturity
- \( \mathbb{Q} \): risk-neutral probability measure
- \( \mathbb{E}^{\mathbb{Q}} \): expectation under the risk-neutral measure

In this demonstration, we simulate the valuation process by calculating the present value of potential future payoffs, illustrating the fundamental role of discounting and probabilistic expectation in derivative pricing.

Understanding this approach helps in grasping how complex derivatives like options are priced using models such as Black-Scholes, which ultimately rely on the principles depicted here.
""")

# Navigation
page = st.sidebar.selectbox(label="Navigation", options=["Overview", "Page 2", "Page 3"])

if page == "Overview":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Page 2":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Page 3":
    # Placeholder for additional pages
    st.write("Page 3 under construction.")

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.")
