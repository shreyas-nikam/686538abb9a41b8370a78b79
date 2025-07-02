
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def calculate_fra_settlement(N, R_K, R_F, d):
    settlement = N * ((R_K - R_F) * (d / 360)) / (1 + R_K * (d / 360))
    return settlement

def run_fra_calculator():
    st.header("Forward Rate Agreement (FRA) Calculator")
    
    st.markdown(r'''
    A Forward Rate Agreement (FRA) is a financial contract where two parties agree on an interest rate for a specified future period. The FRA calculator determines the settlement amount at maturity.
    
    The formula for the FRA settlement is:
    
    $$	ext{Settlement at maturity} = N 	imes rac{(R_K - R_F) 	imes rac{d}{360}}{1 + R_K rac{d}{360}}$$
    
    Where:
    - $N$ is the notional principal amount
    - $R_K$ is the reference interest rate observed at the settlement date
    - $R_F$ is the forward rate specified in the agreement
    - $d$ is the number of days in the contract period
    ''')

    col1, col2 = st.columns(2)

    with col1:
        N = st.number_input("Notional principal amount (N)", min_value=1000.0, value=1000000.0, step=1000.0)
        R_K = st.number_input("Reference interest rate (R_K)", min_value=0.0, max_value=1.0, value=0.05, step=0.001, format="%.3f")

    with col2:
        R_F = st.number_input("Forward rate (R_F)", min_value=0.0, max_value=1.0, value=0.045, step=0.001, format="%.3f")
        d = st.number_input("Number of days in contract period (d)", min_value=1, value=180, step=1)

    if st.button("Calculate FRA Settlement"):
        settlement = calculate_fra_settlement(N, R_K, R_F, d)
        st.success(f"The FRA settlement amount at maturity is: ${settlement:.2f}")

        # Create a range of reference rates for visualization
        ref_rates = np.linspace(max(0, R_K - 0.02), R_K + 0.02, 100)
        settlements = [calculate_fra_settlement(N, r, R_F, d) for r in ref_rates]

        # Plot the settlement amounts
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=ref_rates, y=settlements, mode='lines', name='Settlement Amount'))
        fig.add_vline(x=R_K, line_dash="dash", line_color="red", annotation_text="Current R_K")
        fig.update_layout(title='FRA Settlement Sensitivity to Reference Rate',
                          xaxis_title='Reference Rate (R_K)',
                          yaxis_title='Settlement Amount')
        st.plotly_chart(fig)

        st.markdown('''
        ### Interpretation
        
        The graph above shows how the FRA settlement amount changes with the reference interest rate (R_K):
        
        - When R_K > R_F, the settlement is positive (the FRA buyer receives payment)
        - When R_K < R_F, the settlement is negative (the FRA buyer makes payment)
        - The red dashed line indicates the current R_K value
        
        The steepness of the curve indicates how sensitive the settlement amount is to changes in the reference rate.
        ''')

if __name__ == "__main__":
    run_fra_calculator()
