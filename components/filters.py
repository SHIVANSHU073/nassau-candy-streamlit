import streamlit as st
from services.scenario_service import product_mapping
from services.analysis_service import region_summary, ship_mode_summary

def scenario_filters():
    mapping=product_mapping()
    product=st.selectbox('Product',mapping['product_name'].tolist())
    region=st.selectbox('Destination region',region_summary()['Region'].tolist())
    ship_mode=st.selectbox('Ship mode',ship_mode_summary()['Ship Mode'].tolist())
    return product,region,ship_mode
