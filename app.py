
import streamlit as st

st.set_page_config(page_title="Derivative Price Valuation", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Derivative Price Valuation")
st.divider()

st.markdown("""
# Business Logic Explanation

In this application, we focus on understanding how derivatives are valued, which relies heavily on the concepts of present value, future value, discounted cash flows, and interest calculations. 

The valuation of derivatives often involves projecting future payoffs and discounting them back to their present value using appropriate discount rates. 

**Fundamental formulas involved:**

**Simple Interest:**

\[
FV = P(1 + rt)
\]

where:
- \(FV\) is the future value,
- \(P\) is the principal,
- \(r\) is the annual interest rate (as decimal),
- \(t\) is the time in years.

**Compound Interest:**

\[
FV = P \left(1 + rac{r}{n}ight)^{nt}
\]

where:
- \(n\) is the number of compounding periods per year.

Understanding how interest compounds over time is crucial for valuing derivatives, especially when modeling underlying asset prices or discount factors.

The app allows the user to input various parameters and visualize how the future value of an investment grows under simple and compound interest assumptions, which parallels how discounting and growth assumptions impact derivative pricing.
""")
# The main user interface
page = st.sidebar.selectbox(label="Navigation", options=["Home Page"])

if page == "Home Page":
    st.header("Derivative Price Valuation")
    st.write("Use this app to understand the effects of simple and compound interest in financial valuation models.")
    st.write("Navigate to the different sections to input parameters, see visualizations, and learn about the formulas involved.")

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.")
