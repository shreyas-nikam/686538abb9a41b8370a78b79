
import pandas as pd
from typing import Union

def load_uploaded_data(uploaded_file: Union[str, None]) -> pd.DataFrame:
    """
    Loads and preprocesses the uploaded dataset from the user.

    Args:
        uploaded_file (Union[str, None]): Path to the uploaded CSV or data file.

    Returns:
        pd.DataFrame: Validated and cleaned dataset ready for analysis.

    Raises:
        ValueError: If the file is missing, invalid, or data is corrupted.
        FileNotFoundError: If the specified file does not exist.
        pd.errors.EmptyDataError: If the file is empty.
    """
    if not uploaded_file:
        raise ValueError("No file provided.")
    try:
        df = pd.read_csv(uploaded_file)
    except FileNotFoundError:
        raise
    except pd.errors.EmptyDataError:
        return pd.DataFrame()
    except ValueError as e:
        # Handles invalid format or corrupted data
        raise ValueError(f"Invalid file or data: {e}")
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")

    if df.empty:
        return df

    for col in df.select_dtypes(include=['number']).columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df.dropna(inplace=True)

    return df
