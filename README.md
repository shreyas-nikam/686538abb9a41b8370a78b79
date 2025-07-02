
# Derivative Price Valuation Lab

This Streamlit application provides an interactive platform for exploring derivative pricing models and concepts. The lab covers the following topics:

1. Binomial Option Pricing Model
2. Put-Call Parity
3. Forward Pricing
4. Forward Rate Agreement (FRA) Calculator

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

### Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/derivative-price-valuation-lab.git
   cd derivative-price-valuation-lab
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

To run the Streamlit app locally, use the following command:

The application will open in your default web browser.

## Docker Support

This application can also be run using Docker. To build and run the Docker container:

1. Build the Docker image:
   ```
   docker build -t derivative-price-valuation-lab .
   ```

2. Run the container:
   ```
   docker run -p 8501:8501 derivative-price-valuation-lab
   ```

The application will be accessible at `http://localhost:8501`.

## Usage

Navigate through the different pages using the sidebar to explore various derivative pricing concepts:

- **Binomial Option Pricing**: Calculate option prices using the binomial model and visualize price sensitivity.
- **Put-Call Parity**: Explore the relationship between put and call option prices.
- **Forward Pricing**: Calculate forward prices and visualize their relationship with spot prices.
- **FRA Calculator**: Compute settlement amounts for Forward Rate Agreements and analyze rate sensitivity.

Each page provides interactive inputs, calculations, and visualizations to help understand the underlying concepts.

## License

This project is licensed under the MIT License.

## Acknowledgments

This lab was created as an educational tool for QuantUniversity. It is intended for illustrative and educational purposes only.
