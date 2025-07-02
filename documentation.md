id: 686538abb9a41b8370a78b79_documentation
summary: Derivative Price Valuation Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Derivative Price Valuation Codelab

This codelab guides you through a Streamlit application designed to illustrate the fundamental principles of derivative price valuation. We'll explore how derivatives, financial contracts whose value is derived from underlying assets, are priced using the concept of discounting future expected cash flows to their present value. Understanding these principles is crucial for anyone working with financial instruments, risk management, or trading strategies. This application serves as an educational tool to help you grasp these concepts.

## Setting Up the Environment
Duration: 00:05

Before diving into the application, make sure you have the necessary libraries installed. This application uses Streamlit, NumPy, Pandas, and Plotly. You can install them using pip:

```bash
pip install streamlit numpy pandas plotly
```

## Understanding the `app.py` Structure
Duration: 00:10

The `app.py` file serves as the main entry point for the Streamlit application. Let's break down its structure:

```python
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
```

Key components:

*   **Import Statements:** Imports necessary libraries like Streamlit (`streamlit as st`), and other page modules.
*   **Page Configuration:** Sets the page title and layout using `st.set_page_config`.
*   **Sidebar:**  Adds an image, title, and navigation selectbox to the sidebar.
*   **Title and Introduction:** Displays the main title and an introductory explanation of derivative pricing, including the core formula.
*   **Navigation:** Uses `st.sidebar.selectbox` to create a navigation menu, allowing users to switch between different pages of the application.
*   **Page Routing:** Based on the selected page, the application imports and runs the corresponding function from the `application_pages` directory (`page1.py`, `page2.py`).
*   **Copyright and Disclaimer:**  Includes copyright information and a disclaimer at the bottom of the page.

## Running the Application
Duration: 00:02

To run the application, navigate to the directory containing `app.py` in your terminal and execute the following command:

```bash
streamlit run app.py
```

This will start the Streamlit server and open the application in your web browser.

## Exploring `application_pages/page1.py` - Overview of Derivative Pricing
Duration: 00:15

The `page1.py` file provides an overview of derivative pricing concepts. Let's examine the code:

```python
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def run_page1():
    st.title("Overview of Derivative Pricing")

    st.markdown("""
    ## Understanding Derivative Valuation

    Derivative valuation is a critical aspect of financial engineering. Derivatives, such as options and futures, derive their value from an underlying asset. The most common methods for valuing derivatives involve calculating the expected payoff at a future date and discounting it back to the present.

    ### Core Concepts

    1.  **Risk-Neutral Valuation**: Assumes that investors are indifferent to risk and only require a return equal to the risk-free rate.
    2.  **Discounted Cash Flows (DCF)**: Determines the present value of expected future cash flows.

    ### Formulas and Explanations

    #### Present Value Formula
    The present value (\(PV\)) of a future cash flow is calculated as:

    $$
    PV = \frac{CF}{(1 + r)^t}
    $$

    Where:
    *   \(CF\) is the future cash flow,
    *   \(r\) is the discount rate (risk-free rate),
    *   \(t\) is the time to maturity.

    #### Expected Payoff
    The expected payoff is the weighted average of potential payoffs, using risk-neutral probabilities:

    $$
    \mathbb{E}[\text{Payoff}] = \sum_{i=1}^{n} p_i \cdot \text{Payoff}_i
    $$

    Where:
    *   \(p_i\) is the risk-neutral probability of outcome \(i\),
    *   \(\text{Payoff}_i\) is the payoff for outcome \(i\).

    ### Interactive Example

    Let's consider a simple example: a derivative that pays \$100 if a stock price exceeds a certain level in one year. We assume a risk-free rate of 5%.
    """)

    # Input parameters
    probability = st.slider("Probability of exceeding level:", 0.0, 1.0, 0.5)
    risk_free_rate = st.slider("Risk-free rate:", 0.0, 0.1, 0.05)

    # Calculate expected payoff
    expected_payoff = probability * 100

    # Calculate present value
    present_value = expected_payoff / (1 + risk_free_rate)

    st.write(f"Expected Payoff: ${expected_payoff:.2f}")
    st.write(f"Present Value: ${present_value:.2f}")

    # Visualization
    data = {'Scenario': ['Expected Payoff', 'Present Value'],
            'Value': [expected_payoff, present_value]}
    df = pd.DataFrame(data)

    fig = px.bar(df, x='Scenario', y='Value', title='Expected Payoff vs Present Value')
    st.plotly_chart(fig)
```

This page explains the core concepts of derivative valuation: risk-neutral valuation and discounted cash flows.  It presents the formulas for present value and expected payoff.

**Interactive Elements:**

*   **Sliders:** Uses `st.slider` to allow users to adjust the probability of exceeding a certain level and the risk-free rate.
*   **Calculations:** Calculates the expected payoff and present value based on the user-defined inputs.
*   **Output:** Displays the calculated expected payoff and present value using `st.write`.
*   **Visualization:** Creates a bar chart using Plotly to visualize the expected payoff versus the present value.

## Exploring `application_pages/page2.py` - Advanced Derivative Concepts
Duration: 00:10

The `page2.py` file introduces more advanced concepts in derivative pricing, such as volatility and correlation.

```python
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def run_page2():
    st.title("Advanced Derivative Concepts")

    st.markdown("""
    ## Exploring More Complex Derivatives

    This page delves into some more advanced concepts in derivative pricing, including the impact of volatility and correlation.

    ### Volatility and Option Pricing

    Volatility, a measure of the price fluctuations of an underlying asset, plays a crucial role in option pricing. Higher volatility generally increases option prices, as it increases the potential range of outcomes.

    The Black-Scholes model is a cornerstone of option pricing theory:

    $$
    C = S N(d_1) - K e^{-rT} N(d_2)
    $$

    Where:
    *   \(C\) is the call option price,
    *   \(S\) is the current stock price,
    *   \(K\) is the option's strike price,
    *   \(r\) is the risk-free interest rate,
    *   \(T\) is the time to maturity,
    *   \(N(x)\) is the cumulative standard normal distribution function,
    *   \(d_1\) and \(d_2\) are model-specific parameters.

    ### Correlation and Multi-Asset Derivatives

    Correlation measures the degree to which two assets move together. In multi-asset derivatives, such as basket options, correlation significantly impacts the price.

    """)

    # Placeholder for interactive components or advanced visualizations
    st.write("Further interactive examples and visualizations are under development.")
```

This page discusses the role of volatility in option pricing and introduces the Black-Scholes model. It also touches upon the concept of correlation in multi-asset derivatives. Currently, it serves as a placeholder for future interactive examples and visualizations.

## Application Architecture
Duration: 00:05

The application follows a simple modular architecture:

```
derivative_valuation_app/
├── app.py          # Main application file
├── application_pages/
│   ├── page1.py      # Overview of Derivative Pricing
│   └── page2.py      # Advanced Derivative Concepts
```

*   `app.py`:  Handles the overall application structure, including the sidebar navigation and page routing.
*   `application_pages`: A directory containing individual page modules.  This allows for better organization and separation of concerns.

## Extending the Application
Duration: 00:15

You can extend this application by adding more pages and functionalities. Here are some ideas:

*   **Implement Interactive Black-Scholes Model:** Add a page where users can input the parameters for the Black-Scholes model and see the calculated option price.
*   **Visualize Option Payoffs:** Create visualizations of option payoff diagrams.
*   **Simulate Monte Carlo Pricing:** Implement a Monte Carlo simulation for pricing derivatives.
*   **Add more derivative types**: Include functionality to value futures, swaps and other exotic derivatives.

To add a new page:

1.  Create a new Python file in the `application_pages` directory (e.g., `page3.py`).
2.  Define a function in the new file (e.g., `run_page3()`) that contains the content for the page.
3.  Import and call the function in `app.py` within the page routing section.
4.  Add the new page name to the navigation selectbox in `app.py`.

For example:

Create `application_pages/page3.py`:

```python
import streamlit as st

def run_page3():
    st.title("Monte Carlo Simulation")
    st.write("This page will demonstrate Monte Carlo simulation for derivative pricing.")

```

Modify `app.py`:

```python
# Navigation
page = st.sidebar.selectbox(label="Navigation", options=["Overview", "Page 2", "Page 3"])

if page == "Overview":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Page 2":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Page 3":
    from application_pages.page3 import run_page3
    run_page3()
```

This will add a new page named "Page 3" to the navigation menu, which will display the content defined in `page3.py`.

## Conclusion
Duration: 00:03

This codelab provided a step-by-step guide to understanding the structure and functionality of a Streamlit application for derivative price valuation. By exploring the code and following the instructions, you gained insights into the core principles of derivative pricing and how to implement them in a practical application. You also learned how to extend the application with new features and pages. This foundation will enable you to further explore derivative pricing models and develop more sophisticated financial applications.

<aside class="positive">
Remember that this application is for educational purposes. Real-world derivative pricing involves more complex models and considerations.
</aside>
