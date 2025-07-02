
# Derivative Price Valuation Lab

This Streamlit application provides an interactive platform for exploring derivative pricing models. Users can adjust key parameters and visualize the impact on derivative values. The application focuses on key concepts such as binomial option pricing, put-call parity, and forward contracts.

## Features

1. **Binomial Option Pricing Model**: Calculate and visualize option prices using the binomial model.
2. **Put-Call Parity**: Explore the relationship between put and call option prices.
3. **Forward Contracts**: Understand forward pricing and Forward Rate Agreements (FRA).

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-repo/derivative-price-valuation.git
   ```

2. Navigate to the project directory:
   ```
   cd derivative-price-valuation
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:

The application will open in your default web browser.

## Docker

To run the application using Docker:

1. Build the Docker image:
   ```
   docker build -t derivative-price-valuation .
   ```

2. Run the Docker container:
   ```
   docker run -p 8501:8501 derivative-price-valuation
   ```

Access the application by opening a web browser and navigating to `http://localhost:8501`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
