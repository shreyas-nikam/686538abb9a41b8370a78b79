
# Forward Rate Agreement (FRA)

A forward rate agreement is a contract that ensures a specific rate is guaranteed for a future deposit. The settlement amount at maturity is calculated as:

$$\text{Settlement at maturity} = N \times \frac{(R_K - R_F) \times \frac{d}{360}}{1 + R_K \frac{d}{360}}$$

Where:
- $N$: The notional principal
- $R_K$: The interest rate for the term the FRA is trying to cover, observed at the end of the FRA period
- $R_F$: The rate that is in the FRA agreement to be paid
- $d$: Number of days in the FRA period

This formula calculates the difference between the agreed-upon rate and the actual observed rate, adjusted for the time value of money.
