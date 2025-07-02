
# Technical Specifications: Compound Interest Visualizer Streamlit App

## Overview

This document outlines the technical specifications for a Streamlit application designed to visualize and explain the concept of compound interest. The application will allow users to input a principal amount, annual interest rate, and investment duration. It will then calculate and display the future value of the investment, comparing simple and compound interest growth using an interactive chart. This lab idea relates to the **Basics of Derivative Pricing and Valuation**, specifically how the pricing of financial assets is important. Discounted cash flow methods and models, such as the capital asset pricing model and its variations, are useful for determining the prices of financial assets.

## Step-by-Step Development Process

1.  **Setup and Initialization**:
    -   Create a new Python environment (recommended).
    -   Install the required libraries (Streamlit, Pandas, NumPy, Matplotlib/Plotly).
    -   Create a new Python file (e.g., `compound_interest_app.py`).
    -   Import the necessary libraries.

2.  **User Input Components**:
    -   Use Streamlit's `st.number_input` widgets to collect the following user inputs:
        -   Principal amount (initial investment).
        -   Annual interest rate.
        -   Investment duration (in years).
        -   Compounding frequency (monthly or annually) using `st.radio`.

3.  **Calculation Logic**:
    -   Implement functions to calculate:
        -   Future value with simple interest.
        -   Future value with compound interest (monthly and annually).
    -   The required formulas would be:
        -   Simple interest:  $FV = P(1 + rt)$, where $FV$ is the future value, $P$ is the principal, $r$ is the interest rate, and $t$ is the time in years.
        -   Compound interest: $FV = P(1 + \frac{r}{n})^{nt}$, where $n$ is the number of times interest is compounded per year.

4.  **Data Preparation**:
    -   Create a Pandas DataFrame to store the calculated future values for each year/month.
    -   Include columns for:
        -   Time period (year or month).
        -   Simple interest future value.
        -   Compound interest future value.

5.  **Interactive Chart**:
    -   Use Matplotlib or Plotly to create a line chart comparing simple and compound interest growth over time.
    -   Display the chart using `st.pyplot` or `st.plotly_chart`.
    -   Add annotations and tooltips to provide detailed insights on the chart.

6.  **Displaying Results**:
    -   Use `st.write` to display the final future values for both simple and compound interest.
    -   Add a text explanation summarizing the difference between simple and compound interest.

7. **Adding Formula Explanation**
    - Provide an area to explain compound interest with the formula

## Core Concepts and Mathematical Foundations

### Simple Interest

Simple interest is calculated only on the principal amount. It does not take into account the interest earned in previous periods.

**Formula:**

$$

FV = P(1 + rt)

$$

Where:

*   $FV$: Future Value
*   $P$: Principal Amount
*   $r$: Annual Interest Rate (as a decimal)
*   $t$: Time (in years)

**Example:**
If you invest \$1,000 at a simple interest rate of 5% per year for 10 years, the future value would be:

$$

FV = 1000(1 + 0.05 \times 10) = \$1500

$$

### Compound Interest

Compound interest is calculated on the principal amount and also on the accumulated interest of previous periods. This means that you earn interest on your interest.

**Formula:**

$$

FV = P(1 + \frac{r}{n})^{nt}

$$

Where:

*   $FV$: Future Value
*   $P$: Principal Amount
*   $r$: Annual Interest Rate (as a decimal)
*   $n$: Number of times interest is compounded per year
*   $t$: Time (in years)

**Example:**

If you invest \$1,000 at an annual interest rate of 5% compounded annually for 10 years, the future value would be:

$$

FV = 1000(1 + \frac{0.05}{1})^{(1 \times 10)} = \$1628.89

$$

If the same investment is compounded monthly:

$$

FV = 1000(1 + \frac{0.05}{12})^{(12 \times 10)} = \$1647.01

$$

### Real-world Application

Compound interest is a fundamental concept in investing, savings, and loans. Understanding how it works can help you make informed decisions about your money. For example, it can show you the benefit of starting to save early and the impact of different interest rates and compounding frequencies on your long-term investments.

## Required Libraries and Dependencies

*   **Streamlit**: Used for creating the user interface and deploying the application.
    *   Version: (Latest)
    *   Role: UI framework, widget creation, app deployment.
    *   Example: `import streamlit as st`
*   **Pandas**: Used for creating and manipulating dataframes to store calculated values.
    *   Version: (Latest)
    *   Role: Data structure, data manipulation.
    *   Example: `import pandas as pd`
*   **NumPy**: Used for numerical calculations.
    *   Version: (Latest)
    *   Role: Mathematical operations.
    *   Example: `import numpy as np`
*   **Matplotlib** or **Plotly**: Used for creating interactive charts.
    *   Versions: (Latest)
    *   Role: Data visualization.
    *   Example (Matplotlib):
    ```python
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(df['Time'], df['Simple Interest'], label='Simple Interest')
    ax.plot(df['Time'], df['Compound Interest'], label='Compound Interest')
    st.pyplot(fig)
    ```
    *   Example (Plotly):
     ```python
     import plotly.express as px
     fig = px.line(df, x="Time", y=["Simple Interest", "Compound Interest"], title='Simple vs Compound Interest')
     st.plotly_chart(fig)
     ```

## Implementation Details

The application will primarily use the Streamlit library for its user interface and presentation. The core logic will involve defining functions to perform the calculations related to simple and compound interest.

The Pandas library is used to manage the data, which allows for tabular manipulation. Data will then be transferred to Matplotlib or Plotly for interactive visualization.

## User Interface Components

1.  **Title**: A clear title indicating the app's purpose (e.g., "Compound Interest Visualizer").
2.  **Input Forms**:
    *   `st.number_input("Principal Amount", value=1000)`: Numeric input for the initial investment amount.
    *   `st.number_input("Annual Interest Rate (%)", value=5.0)`: Numeric input for the annual interest rate.
    *   `st.number_input("Investment Duration (Years)", value=10)`: Numeric input for the investment duration in years.
    *   `st.radio("Compounding Frequency", options=["Annually", "Monthly"])`: Radio button to select the compounding frequency.
3.  **Interactive Chart**:
    *   A line chart displaying the growth of simple and compound interest over time.
4.  **Output Display**:
    *   `st.write("Future Value (Simple Interest):", simple_interest_fv)`: Displays the calculated future value with simple interest.
    *   `st.write("Future Value (Compound Interest):", compound_interest_fv)`: Displays the calculated future value with compound interest.
5.  **Explanatory Text**:
    *   `st.write("Compound interest earns interest on interest, leading to significant growth over time.")`: Text explaining the concept of compound interest and highlighting its benefits.
6. **Formula Explanation**
    *   `st.markdown("### Compound Interest Formula")`
    *   `st.latex(r"FV = P(1 + \frac{r}{n})^{nt}")`



### Appendix Code

```code
```code
A forward contract is an over-the-counter derivative contract in which two
parties agree that one party, the buyer, will purchase an underlying asset
from the other party, the seller, at a later date at a fixed price they agree
upon when the contract is signed.

A futures contract is a standardized derivative contract created and traded
on a futures exchange in which two parties agree that one party, the buyer,
will purchase an underlying asset from the other party, the seller, at a later
date at a price agreed upon by the two parties when the contract is initi-
ated and in which there is a daily settling of gains and losses and a credit
guarantee by the futures exchange through its clearinghouse.

A swap contract is an over-the-counter derivative contract in which two
parties agree to exchange a series of cash flows whereby one party pays a
variable series that will be determined by an underlying asset or rate and
the other party pays either 1) a variable series determined by a different
underlying asset or rate or 2) a fixed series.

An option is a derivative contract in which one party, the buyer, pays a
sum of money to the other party, the seller or writer, and receives the right
to either buy or sell an underlying asset at a fixed price either on a specific
expiration date or at any time prior to the expiration date.
```
(Page 3)

```code
So =
E(ST)
(1 + r + 2)Τ
```
(Page 6)

```code
E(ST)
So =
- 0 +γ -
(1 + r + 2)Τ
```
(Page 7)

```code
SOA < SOB:
Buy A at SoA
Sell B at SoB
Cash flow = SOB - SoA(> 0)
STA = STB:
Sell A for STA
Buy B for STB
Cash flow = STA – STB(= 0)
```
(Page 9)

```code
Long asset +
Short derivative
Long risk-free
asset (lending)

Long asset +
Short risk-free
asset (borrowing)
=
Long derivative

Short
derivative
+
Short risk-free
asset (borrowing)
Short asset
```
(Page 11)

```code
Fo (T)
So
= (1 + r)
```
(Page 17)

```code
Fo(T) = So(1 + r)T
```
(Page 17)

```code
(1 + r) = Fo (T) + (y − 0)(1 + r)
So
```
(Page 17)

```code
Fo(T) = (So − y + 0)(1 + r)
```
(Page 18)

```code
Fo (T) = So (1 + r) – (γ – 0)(1 + r)
```
(Page 18)

```code
VT(T) = ST - Fo(T)
```
(Page 16)

```code
Vo(T) = 0
```
(Page 16)

```code
V₁(T) = St – Fo(T)(1 + r)-(T-t)
```
(Page 19)

```code
V₁(T) = S₁ − (y − 0)(1 + r)t – Fo(T)(1 + r)−(T−t)
```
(Page 19)

```code
CO
= Max(0,ST – X)
```
(Page 28)

```code
PT = Max(0,X – ST)
```
(Page 28)

```code
Co ≥ Max 0,So - X/(1+r)
```
(Page 34)

```code
Po ≥ Max[0,X/(1+r) - So]
```
(Page 35)

```code
So + Po = co + X/(1 + r)
```
(Page 38)

```code
Fo(T)/(1+r) + Po = co + x/(1 + r)
```
(Page 41)

```code
u =
St
So
d = ST
So
```
(Page 43)

```code
u =
+ πο + (1 − π)
1+r

1+r-d
u-d
```
(Page 44)

```code
ρ. + (1 − π)ρί
Po
=
1+r
```
(Page 45)
