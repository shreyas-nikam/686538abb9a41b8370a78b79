import pytest
from definition_a136e8b065734d96b6228c296e25e004 import calculate_simple_interest_fv

@pytest.mark.parametrize(
    "principal, annual_rate, time_years, expected",
    [
        # --- Valid cases (positive inputs) ---
        (1000.0, 0.05, 10.0, 1500.0),
        (500.0, 0.03, 5.0, 575.0),
        (2500.0, 0.065, 3.5, pytest.approx(3068.75)),
        # Rate as an integer (e.g., 5 means 500%)
        (100.0, 5, 2.0, 1100.0), # 100 * (1 + 5 * 2) = 100 * 11 = 1100.0

        # --- Valid cases (zero inputs) ---
        (0.0, 0.05, 10.0, 0.0),  # Zero principal
        (1000.0, 0.0, 10.0, 1000.0),  # Zero annual_rate
        (1000.0, 0.05, 0.0, 1000.0),  # Zero time_years
        (0.0, 0.0, 0.0, 0.0),  # All zeros
        (0.0, 0.0, 10.0, 0.0), # Zero principal and rate, non-zero time
        (0.0, 0.05, 0.0, 0.0), # Zero principal and time, non-zero rate
        (1000.0, 0.0, 0.0, 1000.0), # Zero rate and time, non-zero principal

        # --- Valid cases (large numbers) ---
        (1_000_000.0, 0.1, 100.0, 11_000_000.0),
        (1e9, 0.01, 200.0, pytest.approx(3e9)), # 1e9 * (1 + 0.01 * 200) = 1e9 * (1 + 2) = 3e9

        # --- Valid cases (small numbers) ---
        (1.0, 0.0001, 1.0, pytest.approx(1.0001)),
        (0.001, 0.01, 0.01, pytest.approx(0.001 * (1 + 0.01 * 0.01))), # 0.001 * (1 + 0.0001) = 0.0010001

        # --- Valid cases (Boolean inputs, treated as 0 or 1 for numeric calculations) ---
        (True, 0.05, 10.0, 1.0 * (1 + 0.05 * 10)), # 1 * 1.5 = 1.5
        (100.0, True, 5.0, 100.0 * (1 + 1 * 5)), # 100 * 6 = 600.0
        (100.0, 0.05, False, 100.0 * (1 + 0.05 * 0)), # 100 * 1 = 100.0
        (True, False, True, 1.0 * (1 + 0 * 1)), # 1.0
        (False, False, False, 0.0), # 0.0 * (1 + 0 * 0) = 0.0

        # --- Invalid value cases (should raise ValueError) ---
        (-1000.0, 0.05, 10.0, ValueError),  # Negative principal
        (1000.0, -0.05, 10.0, ValueError),  # Negative annual_rate
        (1000.0, 0.05, -10.0, ValueError),  # Negative time_years
        (-100.0, -0.01, 1.0, ValueError),   # Principal and rate negative
        (-100.0, 0.01, -1.0, ValueError),   # Principal and time negative
        (100.0, -0.01, -1.0, ValueError),   # Rate and time negative
        (-100.0, -0.01, -1.0, ValueError),  # All negative inputs

        # --- Invalid type cases (should raise TypeError) ---
        ("1000", 0.05, 10.0, TypeError),  # Principal as string
        (1000.0, "0.05", 10.0, TypeError),  # Annual rate as string
        (1000.0, 0.05, "10", TypeError),  # Time as string
        (None, 0.05, 10.0, TypeError),  # Principal as None
        (1000.0, None, 10.0, TypeError),  # Annual rate as None
        (1000.0, 0.05, None, TypeError),  # Time as None
        ([1000], 0.05, 10.0, TypeError),  # Principal as list
        (1000.0, (0.05,), 10.0, TypeError),  # Annual rate as tuple
        (1000.0, 0.05, {10: "years"}, TypeError),  # Time as dictionary
        (1000.0, 0.05, set([10]), TypeError), # Time as set
        (b'100', 0.05, 10.0, TypeError), # Principal as bytes
        (complex(1, 2), 0.05, 10.0, TypeError), # Principal as complex number
        (1000.0, complex(0, 1), 10.0, TypeError), # Rate as complex number
    ]
)
def test_calculate_simple_interest_fv(principal, annual_rate, time_years, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calculate_simple_interest_fv(principal, annual_rate, time_years)
    else:
        result = calculate_simple_interest_fv(principal, annual_rate, time_years)
        assert result == expected