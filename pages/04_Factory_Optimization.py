import streamlit as st
from services.scenario_service import scenario_predictions, factories
from components.filters import scenario_filters
from components.warnings import show_global_warnings
st.title('Factory Optimization Simulator'); show_global_warnings()
product,region,ship_mode=scenario_filters()
year=st.selectbox('Scenario order year',[2024,2025],index=1)
month=st.slider('Scenario order month',1,12,6)
out,current=scenario_predictions(product,region,ship_mode,year,month)
st.write(f'**Current factory:** {current}')
st.dataframe(out,use_container_width=True,hide_index=True)
st.warning('Every alternative-factory row is a model-based counterfactual proxy. It is not historical evidence that the product can be reassigned or that the predicted difference will occur.')
st.dataframe(factories(),use_container_width=True,hide_index=True)
