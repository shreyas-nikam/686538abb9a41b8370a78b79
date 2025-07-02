
# Technical Specifications for a Streamlit Application: Derivative Pricing Explorer

## Overview

This Streamlit application provides an int\fractive platform for exploring derivative pricing models. Users can upload synthetic datasets, adjust key parameters, and visualize the impact on derivative values. The application focuses on key concepts such as binomial option pricing and put-call parity, presenting them in an accessible and engaging manner.

## Step-by-Step Development Process

1.  **Setup:** Initialize a new Streamlit application using `streamlit run your_app_name.py`.
2.  **Data Input:** Implement a file upload component using `st.file_uploader` to allow users to upload their synthetic datasets (e.g., CSV files).
3.  **Data Processing:** Use `pandas` to load and preprocess the uploaded data. Ensure data validation to prevent errors.
4.  **Parameter Input:** Create int\fractive widgets using `st.slider`, `st.number_input`, and `st.selectbox` to allow users to adjust parameters like risk-free rate, volatility, and strike price.
5.  **Pricing Model Implementation:** Implement derivative pricing models, including the binomial option pricing model and calculations for put-call parity.
6.  **Visualization:** Generate dynamic charts using `plotly` or `matplotlib` to visualize derivative prices and their sensitivity to parameter changes.
7.  **Output and Explanation:** Display calculated derivative values and provide concise explanations of the results and their implications.
8.  **Documentation:** Add inline help and tooltips using `st.help` and `st.markdown` to guide users through the application and explain the underlying concepts.

## Core Concepts and Mathematical Foundations

### Binomial Option Pricing Model
The binomial option pricing model calculates the theoretical value for options. It is done by repeatedly evaluating the option based on a given binomial tree. The risk-neutral probability is first calculated, then the call price:
$$
C_0 = \frac{\pi C_u + (1 - \pi) C_d}{1 + r}
$$
Where:
- $C_0$: Call option price at time 0
- $C_u$: Call option price if the underlying asset price goes up
- $C_d$: Call option price if the underlying asset price goes down
- $\pi$: Risk-neutral probability of an upward move
- $r$: Risk-free interest rate

The risk-neutral probability is calculated as:
$$
\pi = \frac{1 + r - d}{u - d}
$$
Where:
- $u$: Up factor (multiplier for the underlying asset price if it goes up)
- $d$: Down factor (multiplier for the underlying asset price if it goes down)

The binomial option pricing model simplifies the option pricing process, especially for illustrating how changes in the underlying asset's price affect the option value over discrete time intervals.

### Put-Call Parity

Put-Call Parity establishes a relationship between European put and call options with the same strike price and expiration date. The parity condition is given by:
$$
S_0 + P_0 = c_0 + \frac{X}{(1 + r)^T}
$$
Where:
- $S_0$: Current price of the underlying asset
- $P_0$: Current price of the European put option
- $c_0$: Current price of the European call option
- $X$: Strike price of the options
- $r$: Risk-free interest rate
- $T$: Time to expiration

Put-Call Parity demonstrates the interrelation of put and call option prices, which is crucial for understanding arbitrage opportunities and the overall consistency of option pricing.

### Forward Price Formula
The forward price is used in forward con\fracts and determines the price today at which an asset can be bought at a future date.
$$
F_0 = S_0(1 + r)^T
$$
Where:
- $F_0$: Forward price
- $S_0$: Current spot price
- $r$: Risk-free rate
- $T$: Time until expiration

This pricing model provides a way to understand how current prices are determined for future transactions, accounting for the time value of money.

### Forward Rate Agreement (FRA)
A forward rate agreement is a con\fract that ensures a specific rate is guaranteed for a future deposit.
$$
\text{Settlement at maturity} = N \times  \\frac{(R_K - R_F) \times  \\frac{d}{360}}{1 + R_K  \\frac{d}{360}}
$$
Where:
- $N$: The notional principal
- $R_k$: The interest rate for the term the FRA is trying to cover, observed at the end of the FRA period
- $R_F$: The rate that is in the FRA agreement to be paid
- $d$: number of days

These help hedge the user against interest rate volatility and are important for banks that are trying to hedge against changes to interest rates.

## Required Libraries and Dependencies

*   **streamlit**: For building the int\fractive user interface.
*   **pandas**: For data loading, manipulation, and preprocessing.
*   **numpy**: For numerical computations required in pricing models.
*   **plotly** or **matplotlib**: For creating dynamic visualizations.

**Example Imports:**

```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px # Or matplotlib.pyplot as plt
```

## Implementation Details

The application will consist of several modules:

*   **Data Input Module**: Handles file uploads and data loading using `pandas`.
*   **Parameter Input Module**: Implements int\fractive widgets to allow users to adjust key parameters.
*   **Pricing Models Module**: Contains functions implementing the binomial option pricing model, put-call parity calculation, and other relevant models.
*   **Visualization Module**: Generates dynamic charts to visualize derivative prices and sensitivities.
*   **Main Application Module**: Orchestrates the application flow, integrating the other modules and displaying the results.

## User Interface Components

*   **File Uploader**: A `st.file_uploader` component to upload the synthetic dataset.
*   **Numerical Inputs**: `st.number_input` components for specifying parameters like risk-free rate, volatility, and strike price.
*   **Select Box**: `st.selectbox` for selecting the derivative type (e.g., call, put).
*   **Button**: A `st.button` component to trigger the calculation.
*   **Plotly Charts**: `plotly.express` (or `matplotlib.pyplot`) charts displaying derivative prices and sensitivities.
*   **Text Output**: `st.write` components displaying calculated derivative values and explanations.
*   **Help**: `st.help` components and markdown text providing inline documentation and explanations.



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
E(ST)
So =
- 0 +γ -
(1 + r + 2)Τ
```
Reference: Page 7

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
π =
1+r-d
u-d
```
Reference: Page 44

```code
πο + (1 − π)
CO =
1+r
```
Reference: Page 44

```code
Po
=
πρ. + (1 − π)ρί
1+r
```
Reference: Page 45

```code
Co ≥ co
Po ≥ Po
```
Reference: Page 47

```code
Co = Max(0,So - X)
Po = Max(0,X – So)
```
Reference: Page 47

```code
Co ≥ Max[0,So - X/(1+r)]
```
Reference: Page 47

```code
Po ≥ Max 0,X/(1+r) - So]
```
Reference: Page 47
