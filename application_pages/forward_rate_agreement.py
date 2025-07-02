
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def calculate_fra_settlement(N, R_K, R_F, d):
    return N * (R_K - R_F) * (d / 360) / (1 + R_K * (d / 360))

def run_forward_rate_agreement():
    st.header("Forward Rate Agreement (FRA)")
    
    st.markdown(r'''
    A Forward Rate Agreement (FRA) is a contract that ensures a specific rate is guaranteed for a future deposit. It's used to hedge against interest rate volatility.

    The settlement amount at maturity for an FRA is calculated as:

    $$\text{Settlement} = N \times \frac{(R_K - R_F) \times \frac{d}{360}}{1 + R_K \frac{d}{360}}$$

    Where:
    - $N$ is the notional principal
    - $R_K$ is the reference rate observed at the settlement date
    - $R_F$ is the fixed rate agreed in the FRA
    - $d$ is the number of days in the contract period

    This formula determines the amount to be paid at settlement to compensate for the difference between the agreed rate and the actual rate.
    ''')

    # User inputs
    N = st.number_input("Notional principal", min_value=1000.0, value=1000000.0)
    R_F = st.number_input("Fixed rate agreed in FRA", min_value=0.0, max_value=1.0, value=0.05)
    d = st.number_input("Number of days in contract period", min_value=1, value=90)
    R_K = st.number_input("Reference rate observed at settlement", min_value=0.0, max_value=1.0, value=0.06)

    if st.button("Calculate FRA Settlement"):
        settlement = calculate_fra_settlement(N, R_K, R_F, d)
        st.success(f"The FRA settlement amount is: ${settlement:.2f}")

        # Visualization
        reference_rates = np.linspace(0, 0.1, 100)
        settlements = [calculate_fra_settlement(N, r, R_F, d) for r in reference_rates]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=reference_rates, y=settlements, mode='lines', name='FRA Settlement'))
        fig.update_layout(title='FRA Settlement Amount vs Reference Rate',
                          xaxis_title='Reference Rate',
                          yaxis_title='Settlement Amount')
        st.plotly_chart(fig)

        st.markdown('''
        The graph above illustrates how the settlement amount changes with the reference rate. 
        When the reference rate is higher than the fixed rate, the settlement amount is positive 
        (paid to the buyer). When it's lower, the settlement amount is negative (paid by the buyer).
        ''')

if __name__ == "__main__":
    run_forward_rate_agreement()
