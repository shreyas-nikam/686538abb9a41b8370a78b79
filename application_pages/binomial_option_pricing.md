
# Binomial Option Pricing Model

The binomial option pricing model calculates the theoretical value for options by repeatedly evaluating the option based on a given binomial tree. The risk-neutral probability is first calculated, then the call price:

$$C_0 = \frac{\pi C_u + (1 - \pi) C_d}{1 + r}$$

Where:
- $C_0$: Call option price at time 0
- $C_u$: Call option price if the underlying asset price goes up
- $C_d$: Call option price if the underlying asset price goes down
- $\pi$: Risk-neutral probability of an upward move
- $r$: Risk-free interest rate
