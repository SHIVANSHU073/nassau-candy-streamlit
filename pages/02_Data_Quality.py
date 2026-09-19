import streamlit as st
from services.analysis_service import audit
from components.warnings import show_global_warnings
st.title('Data Quality'); show_global_warnings()
a=audit()
for k,v in a.items(): st.write(f'**{k.replace("_"," ").title()}**: {v}')
st.markdown('### Interpretation')
st.write('The dataset has no missing cells or duplicate rows, and Gross Profit reconciles to Sales minus Cost. The major issue is the recorded date relationship: order dates are in 2024–2025 while ship dates are in 2026–2030.')
