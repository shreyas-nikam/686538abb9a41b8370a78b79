
# Derivative Price Valuation Lab

This Streamlit application provides an interactive platform for exploring derivative pricing models. Users can adjust key parameters and visualize the impact on derivative values. The application focuses on key concepts such as binomial option pricing, put-call parity, forward pricing, and forward rate agreements.

## Features

1. Binomial Option Pricing Model
2. Put-Call Parity
3. Forward Price Formula
4. Forward Rate Agreement (FRA)

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## Docker

To run the application using Docker:

1. Build the Docker image:
   ```
   docker build -t derivative-pricing-lab .
   ```
2. Run the Docker container:
   ```
   docker run -p 8501:8501 derivative-pricing-lab
   ```

## Usage

Navigate through the different pages using the sidebar. Each page allows you to input parameters and visualize the results of the corresponding pricing model.

## License

© 2025 QuantUniversity. All Rights Reserved.

The purpose of this demonstration is solely for educational use and illustration. Any reproduction of this demonstration requires prior written consent from QuantUniversity.
