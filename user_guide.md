id: 686538abb9a41b8370a78b79_user_guide
summary: Derivative Price Valuation User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Derivative Price Valuation Codelab

This codelab will guide you through a Streamlit application designed to illustrate the fundamental principles behind derivative pricing. Derivatives are financial contracts whose value is derived from an underlying asset. Understanding how these instruments are priced is crucial for anyone involved in finance, trading, or risk management. This application focuses on demonstrating how derivative prices are computed using models based on the principle of discounting future expected cash flows to present value. We'll explore how factors like risk-free rates and probabilities influence the valuation process.

## Understanding the Core Concept
Duration: 00:05

This application highlights the core concept of derivative valuation: determining the present value of future expected payoffs. The fair price of a derivative is essentially the present value of its expected payoffs under a risk-neutral measure, discounted at the appropriate risk-free rate. The fundamental formula driving this is:

$$
V_0 = e^{-r T} \mathbb{E}^{\mathbb{Q}}[ \text{Payoff at } T ]
$$

Where each component plays a vital role:

*   \( V_0 \): The current value of the derivative - what we're trying to determine.
*   \( r \): The risk-free interest rate - the rate of return for a riskless investment.
*   \( T \): Time to maturity - how long until the derivative expires.
*   \( \mathbb{Q} \): Risk-neutral probability measure - probabilities adjusted to reflect risk preferences.
*   \( \mathbb{E}^{\mathbb{Q}} \): Expectation under the risk-neutral measure - the average payoff, weighted by risk-neutral probabilities.

The application simulates this valuation process, demonstrating the impact of discounting and probabilistic expectation.

## Navigating the Application
Duration: 00:02

The application has a simple navigation structure in the sidebar. You'll find a `selectbox` labeled "Navigation" with options to jump between different sections. Currently, you can choose between "Overview", "Page 2", and "Page 3". Each page explores different aspects of derivative pricing.

<aside class="positive">
 Use the sidebar to quickly jump between different modules of the application.
</aside>

## Exploring the Overview Page
Duration: 00:10

The "Overview" page provides an introduction to derivative valuation and allows you to interact with the core formula. It will introduce you to the concepts of risk-neutral valuation and discounted cash flows. The page includes an interactive example where you can adjust the probability of a certain event occurring and the risk-free rate, and observe the impact on the expected payoff and present value.

1.  **Probability of Exceeding Level:** This slider allows you to set the probability of the derivative paying out \$100. By modifying this you directly influence the expected payoff.
2.  **Risk-free rate:** This slider adjusts the risk-free interest rate which in turn impacts the discounting of the expected payoff, and therefore the present value of the derivative.

The application calculates and displays the expected payoff and the present value based on your inputs. A bar chart visually represents the difference between these two values.

<aside class="negative">
 Remember that this is a simplified model. Real-world derivative pricing can involve much more complex calculations.
</aside>

## Understanding Present Value Calculations
Duration: 00:05

On the "Overview" page, observe how changing the risk-free rate affects the present value. A higher risk-free rate results in a lower present value, due to the increased discounting. The present value \(PV\) of a future cash flow \(CF\) is calculated using the formula:

$$
PV = \frac{CF}{(1 + r)^t}
$$

Where \(r\) is the discount rate (risk-free rate) and \(t\) is the time to maturity.

The Expected Payoff is calculated using:
$$
\mathbb{E}[\text{Payoff}] = \sum_{i=1}^{n} p_i \cdot \text{Payoff}_i
$$

Where \(p_i\) is the risk-neutral probability of outcome \(i\), and \(\text{Payoff}_i\) is the payoff for outcome \(i\).

## Exploring Advanced Derivative Concepts
Duration: 00:03

Navigate to "Page 2" using the sidebar. This page introduces more complex concepts such as the impact of volatility on option pricing and the role of correlation in multi-asset derivatives. This page provides a brief introduction to the Black-Scholes model, a cornerstone of option pricing theory. The core formula is:

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

<aside class="positive">
 Page 2 provides an overview of advanced concepts. Interactive examples for these concepts are under development.
</aside>

## Conclusion and Further Exploration
Duration: 00:02

This codelab provided a walkthrough of the Derivative Price Valuation application, highlighting the core principles of derivative pricing. You learned how to calculate present values based on expected payoffs and risk-free rates. The application showcases the fundamental role of discounting and probabilistic expectation in valuing derivatives. While "Page 3" is currently under construction, feel free to revisit the application as it evolves with new features and interactive examples.
