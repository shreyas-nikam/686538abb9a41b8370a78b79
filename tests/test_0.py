import pytest
from definition_157684f6dd064ec48c93b909e43d434f import calculate_simple_interest_fv

@pytest.mark.parametrize("principal, annual_rate, time_years, expected", [
    # Happy Path: Valid inputs
    (1000.0, 0.05, 10, 1500.0),  # Example from simple interest formula spec
    (5000.0, 0.03, 5, 5750.0),   # Another standard positive case
    (100.0, 0.01, 1, 101.0),     # Smallest non-zero time, small rate
    (0.0, 0.05, 10, 0.0),        # Zero principal: FV should be 0
    (1000.0, 0.0, 10, 1000.0),   # Zero annual rate: FV should be principal
    (1000.0, 0.05, 0, 1000.0),   # Zero time: FV should be principal
    (0.0, 0.0, 0, 0.0),          # All zeros
    (1234.56, 0.0789, 7, 1234.56 * (1 + 0.0789 * 7)), # Mixed floats and int
    (1_000_000.0, 0.1, 50, 6_000_000.0), # Large principal, rate, and time
    (10.0, 0.001, 100, 11.0),    # Small annual rate, long time
    (1_000_000_000.0, 0.00000001, 1_000_000_000, 1_000_000_010.0), # Extreme values where r*t is small
    (2000, 0.02, 3, 2000 * (1 + 0.02 * 3)), # Principal and rate as int (should be implicitly cast to float)
    (999.99, 0.0001, 1, 999.99 * (1 + 0.0001 * 1)), # Very small rate and time
])
def test_calculate_simple_interest_fv_valid_inputs(principal, annual_rate, time_years, expected):
    """
    Test cases for valid inputs to calculate_simple_interest_fv.
    """
    assert calculate_simple_interest_fv(principal, annual_rate, time_years) == pytest.approx(expected)

@pytest.mark.parametrize("principal, annual_rate, time_years, expected_exception", [
    # Error Handling: Invalid values (negative principal, rate, time)
    # For investment context, these should typically be non-negative.
    (-100.0, 0.05, 10, ValueError), # Negative principal
    (1000.0, -0.05, 10, ValueError), # Negative annual rate
    (1000.0, 0.05, -10, ValueError), # Negative time
    (-1.0, -0.01, -1, ValueError),  # All negative combination
    
    # Error Handling: Invalid types for 'time_years' (must be int as per docstring)
    (100.0, 0.05, 10.5, TypeError),  # Time as float
    (100.0, 0.05, "10", TypeError),  # Time as string
    (1000.0, 0.05, None, TypeError), # Time as None
    (1000.0, 0.05, [10], TypeError), # Time as list
    (1000.0, 0.05, {}, TypeError), # Time as dict

    # Error Handling: Invalid types for 'principal' (must be float or int)
    ("1000", 0.05, 10, TypeError),  # Principal as string
    (None, 0.05, 10, TypeError),    # Principal as None
    ([1000], 0.05, 10, TypeError),  # Principal as list
    ({"P":1000}, 0.05, 10, TypeError), # Principal as dict

    # Error Handling: Invalid types for 'annual_rate' (must be float or int)
    (1000.0, "0.05", 10, TypeError), # Annual rate as string
    (1000.0, None, 10, TypeError),  # Annual rate as None
    (1000.0, {"rate":0.05}, 10, TypeError), # Annual rate as dict
])
def test_calculate_simple_interest_fv_invalid_inputs(principal, annual_rate, time_years, expected_exception):
    """
    Test cases for invalid inputs (type errors or value errors) to calculate_simple_interest_fv.
    """
    with pytest.raises(expected_exception):
        calculate_simple_interest_fv(principal, annual_rate, time_years)
