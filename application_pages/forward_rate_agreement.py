
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def calculate_fra_settlement(N, R_K, R_F, d):
    return N * ((R_K - R_F) * (d / 360)) / (1 + R_K * (d / 360))

def run_forward_rate_agreement():
    st.header("Forward Rate Agreement (FRA)")
    
    st.markdown(r'''
    A Forward Rate Agreement (FRA) is a contract that guarantees a specific interest rate for a future deposit or loan. The settlement amount at maturity is calculated using the formula:

    $$\text{Settlement} = N \times \frac{(R_K - R_F) \times \frac{d}{360}}{1 + R_K \times \frac{d}{360}}$$

    Where:
    - $N$ is the notional principal amount
    - $R_K$ is the reference interest rate observed at the settlement date
    - $R_F$ is the fixed interest rate agreed in the FRA
    - $d$ is the number of days in the contract period

    This formula determines the amount to be paid at the settlement date to compensate for the difference between the agreed rate and the actual rate.
    ''')

    # User inputs
    N = st.number_input("Notional principal amount", min_value=1000, value=1000000, step=1000)
    R_F = st.number_input("Fixed interest rate (R_F)", min_value=0.0, max_value=0.2, value=0.05, step=0.001, format="%.3f")
    d = st.number_input("Number of days in the contract period", min_value=1, value=90, step=1)

    if st.button("Calculate FRA Settlement"):
        # Create a range of possible reference rates
        R_K_range = np.linspace(max(0, R_F - 0.05), R_F + 0.05, 100)
        settlements = [calculate_fra_settlement(N, R_K, R_F, d) for R_K in R_K_range]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=R_K_range, y=settlements, mode='lines', name='Settlement Amount'))
        fig.update_layout(title='FRA Settlement Amount vs Reference Rate',
                          xaxis_title='Reference Rate (R_K)',
                          yaxis_title='Settlement Amount')
        st.plotly_chart(fig)

        st.markdown('''
        **Interpretation:**
        - The graph shows how the settlement amount changes with different reference rates (R_K).
        - When R_K > R_F, the settlement is positive, meaning the FRA buyer receives payment.
        - When R_K < R_F, the settlement is negative, meaning the FRA buyer makes a payment.
        - The settlement amount increases as the difference between R_K and R_F increases.
        - This demonstrates how FRAs can be used to hedge against interest rate fluctuations.
        ''')

        # Calculate settlement for current R_F as R_K
        current_settlement = calculate_fra_settlement(N, R_F, R_F, d)
        st.write(f"If the reference rate (R_K) equals the fixed rate (R_F) of {R_F:.3f}, the settlement amount would be: ${current_settlement:.2f}")

