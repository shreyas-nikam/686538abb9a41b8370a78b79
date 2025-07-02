
from numbers import Real

def calculate_simple_interest_fv(principal: float, annual_rate: float, time_years: float) -> float:
    """
    Calculates the future value of an investment using the simple interest formula.
    This method calculates interest only on the initial principal amount, without
    considering accumulated interest from previous periods.

    Arguments:
        principal (float): The initial investment amount. Must be a non-negative real number.
        annual_rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
                             Must be a non-negative real number.
        time_years (float): The duration of the investment in years. Must be a non-negative real number.

    Returns:
        float: The future value of the investment with simple interest.

    Raises:
        TypeError: If any input argument is not a real numeric type (e.g., str, list, None, complex).
        ValueError: If any input argument is negative.
    """
    # Type validation: Ensure all inputs are real numeric types (int, float, bool).
    if not isinstance(principal, Real):
        raise TypeError("Principal must be a real numeric value.")
    if not isinstance(annual_rate, Real):
        raise TypeError("Annual rate must be a real numeric value.")
    if not isinstance(time_years, Real):
        raise TypeError("Time in years must be a real numeric value.")

    # Value validation: Ensure inputs are non-negative.
    # Boolean values (True=1, False=0) are handled correctly as non-negative integers.
    if principal < 0:
        raise ValueError("Principal cannot be negative.")
    if annual_rate < 0:
        raise ValueError("Annual rate cannot be negative.")
    if time_years < 0:
        raise ValueError("Time in years cannot be negative.")

    # Calculate Future Value (FV) using the simple interest formula: FV = P * (1 + R * T)
    # Python's automatic type promotion will ensure floating-point arithmetic is used if necessary.
    future_value = principal * (1 + annual_rate * time_years)

    return float(future_value)


from numbers import Real

def calculate_simple_interest_fv(principal: float, annual_rate: float, time_years: float) -> float:
    """
    Calculates the future value of an investment using the simple interest formula.
    This method calculates interest only on the initial principal amount, without
    considering accumulated interest from previous periods.

    Arguments:
        principal (float): The initial investment amount. Must be a non-negative real number.
        annual_rate (float): The annual interest rate as a decimal (e.g., 0.05 for 5%).
                             Must be a non-negative real number.
        time_years (float): The duration of the investment in years. Must be a non-negative real number.

    Returns:
        float: The future value of the investment with simple interest.

    Raises:
        TypeError: If any input argument is not a real numeric type (e.g., str, list, None, complex).
        ValueError: If any input argument is negative.
    """
    # Type validation: Ensure all inputs are real numeric types (int, float, bool).
    if not isinstance(principal, Real):
        raise TypeError("Principal must be a real numeric value.")
    if not isinstance(annual_rate, Real):
        raise TypeError("Annual rate must be a real numeric value.")
    if not isinstance(time_years, Real):
        raise TypeError("Time in years must be a real numeric value.")

    # Value validation: Ensure inputs are non-negative.
    # Boolean values (True=1, False=0) are handled correctly as non-negative integers.
    if principal < 0:
        raise ValueError("Principal cannot be negative.")
    if annual_rate < 0:
        raise ValueError("Annual rate cannot be negative.")
    if time_years < 0:
        raise ValueError("Time in years cannot be negative.")

    # Calculate Future Value (FV) using the simple interest formula: FV = P * (1 + R * T)
    # Python's automatic type promotion will ensure floating-point arithmetic is used if necessary.
    future_value = principal * (1 + annual_rate * time_years)

    return float(future_value)
