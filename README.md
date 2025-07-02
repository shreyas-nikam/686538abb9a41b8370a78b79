# Derivative Price Valuation Application

## Project Title and Description

This Streamlit application provides an interactive demonstration of derivative price valuation, focusing on the fundamental principles of discounting future expected cash flows. It illustrates how derivative prices are computed using models based on these principles, highlighting the role of risk-free rates, time to maturity, and risk-neutral expectations.  The application is designed for educational purposes and aims to improve understanding of core concepts in financial engineering.

## Features

*   **Interactive Valuation:** Allows users to adjust key parameters like risk-free rates and probabilities to see their effect on derivative prices.
*   **Visualizations:** Presents results through clear and concise charts using Plotly.
*   **Educational Content:** Explains the theoretical background of derivative pricing with LaTeX-formatted formulas.
*   **Modular Design:** Organized into separate pages for easy navigation and expansion.
*   **Overview of Key Concepts:** Covers present value calculations, expected payoff computations, volatility, and correlation in derivative pricing.
*   **Clear Documentation:** Includes descriptive text and formulas to explain the underlying concepts.

## Getting Started

### Prerequisites

Before running the application, ensure you have the following installed:

*   **Python 3.7+**: Download from [python.org](https://www.python.org/)
*   **Pip**: Python package installer (usually comes with Python)

### Installation

1.  **Clone the repository:**

    ```bash
    git clone <your_repository_url>  # Replace with your repository URL if hosted on GitHub or similar. If working locally, skip this step.
    cd derivative-price-valuation
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    # Activate the virtual environment (Windows)
    venv\Scripts\activate
    # Activate the virtual environment (macOS/Linux)
    source venv/bin/activate
    ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file with the following content:

    ```
    streamlit
    numpy
    pandas
    plotly
    ```

## Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2.  **Open the application in your browser:**

    Streamlit will provide a URL (usually `http://localhost:8501`) where you can access the application.

3.  **Interact with the application:**

    *   Use the sidebar navigation to switch between different pages: "Overview", "Page 2", and "Page 3" (Page 3 is under construction).
    *   On each page, adjust the available parameters (e.g., risk-free rate, probability) using the sliders.
    *   Observe the changes in the calculated values and visualizations in real-time.

## Project Structure

```
derivative-price-valuation/
├── app.py                     # Main Streamlit application file
├── application_pages/
│   ├── page1.py               # Code for the "Overview" page
│   ├── page2.py               # Code for the "Page 2" page
│   └── __init__.py           # Makes application_pages a package
├── requirements.txt           # List of Python dependencies
└── README.md                  # This file
```

## Technology Stack

*   **Streamlit:** Used for building the interactive web application.
*   **NumPy:** Used for numerical computations and array manipulation.
*   **Pandas:** Used for data manipulation and analysis.
*   **Plotly:** Used for creating interactive charts and visualizations.
*   **Python:** The primary programming language.

## Contributing

Contributions are welcome! Here's how you can contribute:

1.  **Fork the repository:** Create your own copy of the project.
2.  **Create a branch:** Make your changes in a separate branch.
3.  **Commit your changes:** Write clear and descriptive commit messages.
4.  **Submit a pull request:**  Explain your changes and their purpose.

Please follow these guidelines:

*   Write clean and well-documented code.
*   Adhere to PEP 8 style guidelines.
*   Include tests for new features or bug fixes.
*   Update the documentation as needed.

## License

This project is licensed under the [MIT License](LICENSE) - see the `LICENSE` file for details.

## Contact

For questions, suggestions, or issues, please contact:

*   QuantUniversity: [https://quantuniversity.com/](https://quantuniversity.com/)

**Disclaimer**:  This application is intended for educational purposes only. The results should not be used for financial decision-making without consulting with a qualified professional.  QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.
