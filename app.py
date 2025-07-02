
import streamlit as st

st.set_page_config(page_title="QuLab: Derivative Price Valuation", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab: Derivative Price Valuation")
st.divider()

st.markdown("In this lab, we explore various derivative pricing models and concepts, including the Binomial Option Pricing Model, Put-Call Parity, Forward Price Formula, and Forward Rate Agreement (FRA). This interactive application allows users to upload synthetic datasets, adjust key parameters, and visualize the impact on derivative values.")

st.markdown(r'''
### Key Concepts:

1. **Binomial Option Pricing Model**:
   The binomial option pricing model calculates the theoretical value for options using a binomial tree. The risk-neutral probability is first calculated, then the call price:
   
   $$C_0 = \frac{\pi C_u + (1 - \pi) C_d}{1 + r}$$
   
   Where:
   - $C_0$: Call option price at time 0
   - $C_u$: Call option price if the underlying asset price goes up
   - $C_d$: Call option price if the underlying asset price goes down
   - $\pi$: Risk-neutral probability of an upward move
   - $r$: Risk-free interest rate

2. **Put-Call Parity**:
   Put-Call Parity establishes a relationship between European put and call options with the same strike price and expiration date:
   
   $$S_0 + P_0 = c_0 + \frac{X}{(1 + r)^T}$$
   
   Where:
   - $S_0$: Current price of the underlying asset
   - $P_0$: Current price of the European put option
   - $c_0$: Current price of the European call option
   - $X$: Strike price of the options
   - $r$: Risk-free interest rate
   - $T$: Time to expiration

3. **Forward Price Formula**:
   The forward price formula determines the price today at which an asset can be bought at a future date:
   
   $$F_0 = S_0(1 + r)^T$$
   
   Where:
   - $F_0$: Forward price
   - $S_0$: Current spot price
   - $r$: Risk-free rate
   - $T$: Time until expiration

4. **Forward Rate Agreement (FRA)**:
   A forward rate agreement is a contract that ensures a specific rate is guaranteed for a future deposit:
   
   $$\text{Settlement at maturity} = N \times \frac{(R_K - R_F) \times \frac{d}{360}}{1 + R_K \frac{d}{360}}$$
   
   Where:
   - $N$: The notional principal
   - $R_k$: The interest rate for the term the FRA is trying to cover, observed at the end of the FRA period
   - $R_F$: The rate that is in the FRA agreement to be paid
   - $d$: number of days
''')

st.markdown("Use the navigation menu on the left to explore different aspects of derivative pricing and valuation.")

# Your code starts here
page = st.sidebar.selectbox(label="Navigation", options=["Binomial Option Pricing", "Put-Call Parity", "Forward Pricing", "FRA Calculation"])

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
# Your code ends

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
