
import streamlit as st

st.set_page_config(page_title="QuLab: Derivative Price Valuation", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Derivative Price Valuation")
st.divider()

st.write("In this lab, we explore various derivative pricing models and concepts.")
st.write("Use the navigation menu on the left to explore different aspects of derivative pricing and valuation.")

page = st.sidebar.selectbox("Navigation", ["Binomial Option Pricing", "Put-Call Parity", "Forward Pricing", "FRA Calculation"])

if page == "Binomial Option Pricing":
    from application_pages.binomial_option_pricing import run_binomial_option_pricing
    run_binomial_option_pricing()
elif page == "Put-Call Parity":
    from application_pages.put_call_parity import run_put_call_parity
    run_put_call_parity()
elif page == "Forward Pricing":
    from application_pages.forward_pricing import run_forward_pricing
    run_forward_pricing()
elif page == "FRA Calculation":
    from application_pages.fra_calculation import run_fra_calculation
    run_fra_calculation()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration.")
