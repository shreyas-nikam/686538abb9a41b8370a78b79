
import numbers

def calculate_simple_interest_fv(principal: numbers.Real, annual_rate: numbers.Real, time_years: int) -> float:
    """
    Calculates the future value of an investment using the simple interest formula.
    This formula computes interest only on the initial principal amount.

    Arguments:
        principal (float | int): The initial amount of money invested or borrowed.
        annual_rate (float | int): The annual interest rate as a decimal (e.g., 0.05 for 5%).
        time_years (int): The duration of the investment in years.

    Output:
        float: The future value of the investment.

    Raises:
        TypeError: If principal or annual_rate are not numeric (int or float),
                   or if time_years is not an integer.
        ValueError: If principal, annual_rate, or time_years are negative, as these
                    are typically non-negative in financial contexts.
    """
    # Type validation
    if not isinstance(principal, (int, float)):
        raise TypeError("Principal must be a number (int or float).")
    if not isinstance(annual_rate, (int, float)):
        raise TypeError("Annual rate must be a number (int or float).")
    
    # Specific type validation for time_years as per test cases requirements
    # Disallow floats for time_years explicitly before checking for int,
    # as int check would fail for floats and raise a generic TypeError
    if isinstance(time_years, float):
        raise TypeError("Time in years must be an integer, not a float.")
    if not isinstance(time_years, int):
        raise TypeError("Time in years must be an integer.")

    # Value validation (non-negativity)
    if principal < 0:
        raise ValueError("Principal cannot be negative.")
    if annual_rate < 0:
        raise ValueError("Annual rate cannot be negative.")
    if time_years < 0:
        raise ValueError("Time in years cannot be negative.")

    # Simple interest future value formula: FV = P * (1 + r * t)
    # This is the standard definition of future value with simple interest,
    # where interest is calculated only on the initial principal.
    future_value = principal * (1 + annual_rate * time_years)

    return float(future_value)
