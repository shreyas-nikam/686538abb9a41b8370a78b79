
# Technical Specifications for Derivative Pricing Explorer Streamlit Application

## Overview

This Streamlit application, named "Derivative Pricing Explorer," provides an int\fractive platform for users to explore derivative pricing concepts. Users can upload synthetic datasets, int\fract with visualizations, and conduct scenario analyses to understand the factors influencing derivative valuations. The application implements basic pricing models, such as the binomial model and Put-Call Parity, enhancing comprehension and providing a hands-on learning experience.

## Step-by-Step Development Process

1.  **Setup**: Install necessary libraries (`streamlit`, `pandas`, `matplotlib`, `seaborn`).
2.  **Data Input**: Implement a file uploader using `streamlit.file_uploader` to allow users to upload their synthetic datasets.
3.  **Data Handling**: Use `pandas` to read and preprocess the uploaded data, handling numeric, categorical, and time-series data types appropriately.
4.  **UI Components**: Create int\fractive widgets like sliders and input forms using `streamlit.slider` and `streamlit.number_input` for parameters such as risk-free rate and volatility.
5.  **Pricing Models**: Implement the binomial option pricing model and Put-Call Parity formula in Python functions.
6.  **Visualizations**: Generate dynamic charts (line charts, bar graphs, scatter plots) using `matplotlib` and `seaborn` to display derivative prices and related factors.
7.  **Annotations**: Add annotations and tooltips to charts using `matplotlib` to provide detailed insights and explanations.
8.  **User Int\fraction**: Link UI components to pricing model calculations and visualizations, enabling real-time updates based on user inputs.
9.  **Documentation**: Incorporate inline help and tooltips using `streamlit.markdown` and `streamlit.help` to guide users through the data exploration process.

## Core Concepts and Mathematical Foundations

### Binomial Option Pricing Model

The binomial model is used to calculate the price of options using a discrete-time approach.
$$
C_0 = \\frac{\pi C_u + (1 - \pi) C_d}{1 + r}
$$
Where:
- $C_0$: Call option price at time 0
- $\pi$: Risk-neutral probability of an upward move
- $C_u$: Call option price if the underlying asset price moves up
- $C_d$: Call option price if the underlying asset price moves down
- $r$: Risk-free interest rate

The risk-neutral probability $\pi$ is calculated as:
$$
\pi = \\frac{1 + r - d}{u - d}
$$
Where:
- $u$: Up factor (percentage increase in the asset price)
- $d$: Down factor (percentage decrease in the asset price)

This model simplifies derivative pricing by approximating the price movement of the underlying asset in discrete steps, enabling a clearer understanding of how different scenarios affect the option's value.

### Put-Call Parity
The Put-Call Parity is a relationship between the prices of European put and call options with the same strike price and expiration date.
$$
S_0 + P_0 = c_0 + \\frac{X}{(1 + r)^T}
$$
Where:
- $S_0$: Current price of the underlying asset
- $P_0$: Price of the put option
- $c_0$: Price of the call option
- $X$: Strike price of the options
- $r$: Risk-free interest rate
- $T$: Time to expiration

This formula illustrates the equilibrium relationship between put and call options, demonstrating how the values of the options are interconnected.

### Forward Price Formula

The forward price is the predetermined delivery price for an asset at a specified time in the future.
$$
F_0 = S_0 \cdot e^{rT}
$$
Where:
- $F_0$: Forward price at time 0
- $S_0$: Spot price of the asset at time 0
- $r$: Risk-free interest rate
- $T$: Time to delivery

This formula determines the fair price for a forward con\fract, ensuring no arbitrage opportunities exist between the spot and forward markets.

### Present Value Formula
The present value of future cash flows is calculated using:
$$
PV = \\frac{FV}{(1 + r)^n}
$$
Where:
- $PV$: Present Value
- $FV$: Future Value
- $r$: Discount rate per period
- $n$: Number of periods

This formula determines how much a future sum of money is worth in today's dollars, accounting for the time value of money.

## Required Libraries and Dependencies

-   **Streamlit**: Used for creating the user interface and handling user int\fractions.
    -   Version: Not Specified
    -   Import: `import streamlit as st`
    -   Usage: `st.file_uploader`, `st.slider`, `st.pyplot`, `st.markdown`, etc.
-   **Pandas**: Used for data manipulation and analysis.
    -   Version: Not Specified
    -   Import: `import pandas as pd`
    -   Usage: `pd.read_csv`, `pd.DataFrame`, data preprocessing.
-   **Matplotlib**: Used for creating static, int\fractive, and animated visualizations in Python.
    -   Version: Not Specified
    -   Import: `import matplotlib.pyplot as plt`
    -   Usage: Creating line charts, bar graphs, scatter plots.
-   **Seaborn**: Used for making statistical graphics in Python. It builds on top of Matplotlib and is closely integrated with Pandas data structures.
    -   Version: Not Specified
    -   Import: `import seaborn as sns`
    -   Usage: Enhancing the aesthetics and statistical representation of visualizations.

## Implementation Details

1.  **Data Loading and Preprocessing**:
    -   The application starts with a file uploader component that allows users to upload a synthetic dataset.
    -   Upon uploading, `pandas` reads the data and stores it in a DataFrame.
    -   The application performs data type validation to ensure that all data is of the right format and handles missing values.

2.  **Parameter Input**:
    -   Users can int\fract with UI widgets to set parameters such as the risk-free rate, volatility, strike price, and time to expiration.
    -   These parameters are stored in variables that are used in the calculations.

3.  **Pricing Model Implementation**:
    -   The binomial option pricing model calculates option prices based on the user-defined parameters.
    -   The Put-Call Parity formula is also implemented to demonstrate the relationship between the prices of put and call options.

4.  **Visualizations**:
    -   `Matplotlib` and `Seaborn` are used to generate line charts displaying option prices over time, bar graphs showing the effect of different parameters on option prices, and scatter plots illustrating the relationship between derivative prices and asset prices.

5.  **Real-Time Updates**:
    -   Whenever a user changes a parameter using the UI widgets, the calculations are automatically updated, and the charts are redrawn to reflect the new data.

6.  **Formula Explanations**:
    -   The application provides detailed explanations of each formula, including the variables, their descriptions, and the \fractical application of the formula.

## User Interface Components

1.  **File Uploader**:
    -   Allows users to upload their synthetic datasets.
    -   Type: `st.file_uploader`
    -   Functionality: Accepts CSV files.
2.  **Sliders**:
    -   For adjusting parameters like the risk-free rate and volatility.
    -   Type: `st.slider`
    -   Functionality: Adjusts numeric values within a specified range.
3.  **Number Input Fields**:
    -   For entering specific values such as the strike price.
    -   Type: `st.number_input`
    -   Functionality: Allows users to input numeric values directly.
4.  **Charts**:
    -   Dynamic line charts, bar graphs, and scatter plots generated using `matplotlib` and `seaborn`.
    -   Type: `st.pyplot`
    -   Functionality: Displays derivative prices and their sensitivity to various factors.
5.  **Text Explanations**:
    -   Inline help and tooltips providing definitions, \fractical examples, and explanations of the mathematical concepts.
    -   Type: `st.markdown` and `st.help`
    -   Functionality: Provides guidance and insights to users.
6.  **Int\fractive Tables**:
    -   Displaying processed data and calculation results.
    -   Type: `st.dataframe` or `st.table`
    -   Functionality: Provides a tabular view of relevant data.



### Appendix Code

```code
 ```code
A derivative is a financial instrument that derives its performance from the
performance of an underlying asset.
```
Reference: Page 2
```code
A forward con\fract is an over-the-counter derivative con\fract in which two
parties agree that one party, the buyer, will purchase an underlying asset
from the other party, the seller, at a later date at a fixed price they agree
upon when the con\fract is signed.
```
Reference: Page 3
```code
A futures con\fract is a standardized derivative con\fract created and traded
on a futures exchange in which two parties agree that one party, the buyer,
will purchase an underlying asset from the other party, the seller, at a later
date at a price agreed upon by the two parties when the con\fract is initi-
ated and in which there is a daily settling of gains and losses and a credit
guarantee by the futures exchange through its clearinghouse.
```
Reference: Page 3
```code
A swap con\fract is an over-the-counter derivative con\fract in which two
parties agree to exchange a series of cash flows whereby one party pays a
variable series that will be determined by an underlying asset or rate and
the other party pays either 1) a variable series determined by a different
underlying asset or rate or 2) a fixed series.
```
Reference: Page 3
```code
An option is a derivative con\fract in which one party, the buyer, pays a
sum of money to the other party, the seller or writer, and receives the right
to either buy or sell an underlying asset at a fixed price either on a specific
expiration date or at any time prior to the expiration date.
```
Reference: Page 3
```code
So =
E(ST)
(1 + r + 2)Τ
```
Reference: Page 6
```code
So =
E(ST)
- 0 +γ -
(1 + r + 2)Τ
```
Reference: Page 7
```code
STA = STB:
Sell A for STA
Buy B for STB
Cash flow = STA – STB(= 0)
```
Reference: Page 9
```code
SOA < SOB:
Buy A at SoA
Sell B at SoB
Cash flow = SOB - SoA(> 0)
```
Reference: Page 9
```code
Long asset +
Short derivative
Long risk-free
asset (lending)
Long asset +
Short risk-free
=
Long derivative
asset (borrowing)
Short
+
derivative
Short risk-free
asset (borrowing)
Short asset
```
Reference: Page 11
```code
VT(T) = ST - Fo(T)
```
Reference: Page 16
```code
Vo(T) = 0
```
Reference: Page 16
```code
Fo (T)
So
= (1 + r)
```
Reference: Page 17
```code
Fo(T) = So(1 + r)T
```
Reference: Page 17
```code
(1 + r) = Fo (T) + (y − 0)(1 + r)
So
T
```
Reference: Page 17
```code
Fo(T) = (So − y + 0)(1 + r)
```
Reference: Page 18
```code
Fo (T) = So (1 + r) – (γ – 0)(1 + r)
```
Reference: Page 18
```code
V₁(T) = St – Fo(T)(1 + r)-(T-t)
```
Reference: Page 19
```code
V₁(T) = S₁ − (y − 0)(1 + r)t – Fo(T)(1 + r)−(T−t)
```
Reference: Page 19
```code
CT = Max(0,ST – X)
```
Reference: Page 28
```code
PT = Max(0,X – ST)
```
Reference: Page 28
```code
Co ≥ Max 0,So - X/(1+r)
```
Reference: Page 34
```code
Po ≥ Max[0,X/(1+r) - So]
```
Reference: Page 35
```code
So + Po = co + X/(1 + r)
```
Reference: Page 38
```code
So + Po = co + X/(1 + r)
Fo(T)/(1+r) + Po = co + x/(1 + r)
```
Reference: Page 41
```code
u =
St
So
d = ST
So
```
Reference: Page 43
```code
CO
=
+
πο + (1 − π)
1+r
```
Reference: Page 44
```code
π =
1+r-d
u-d
```
Reference: Page 44
```code
Po
=
πρ. + (1 − π)ρί
1+r
```
Reference: Page 45
