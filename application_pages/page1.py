
import streamlit as st

def run_page1():
    st.header("Introduction to Derivative Valuation")
    st.write("This page provides background on the fundamental concepts used in derivative pricing.")
    st.markdown(""" 
    # Derivatives Overview

    Derivatives are financial instruments whose value depends on the price of underlying assets such as stocks, bonds, commodities, or currencies.

    ## Key Concepts:
    - **Present Value (PV):** The current worth of a future cash flow discounted at a particular rate.
    - **Future Value (FV):** The value of an investment at a future point, considering interest or growth.
    - **Discount Rate:** The rate used to determine PV from FV.
    - **Interest Rates:** Central to valuation models, affecting asset prices and derivative pricing.
    - **No-Arbitrage Principle:** Ensures there are no riskless profit opportunities, guiding models for fair pricing.

    Understanding these concepts is essential for computing fair prices and designing hedging strategies.
    """)
