
# Derivative Price Valuation Lab

This Streamlit application provides an interactive platform for exploring derivative pricing models. Users can adjust key parameters and visualize the impact on derivative values.

## Features

- Binomial Option Pricing Model
- Put-Call Parity
- Forward Price Formula
- Forward Rate Agreement (FRA)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-repo/derivative-price-valuation.git
   cd derivative-price-valuation
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

Run the Streamlit app with:

The application will open in your default web browser.

## Docker

To run the application using Docker:

1. Build the Docker image:
   ```
   docker build -t derivative-price-valuation .
   ```

2. Run the container:
   ```
   docker run -p 8501:8501 derivative-price-valuation
   ```

3. Open your web browser and navigate to `http://localhost:8501`

## Usage

Navigate through different pricing models using the sidebar. Adjust parameters using the interactive widgets and observe how they affect the derivative prices and charts.

## License

© 2025 QuantUniversity. All Rights Reserved.

This demonstration is solely for educational use and illustration. Any reproduction of this demonstration requires prior written consent from QuantUniversity.
