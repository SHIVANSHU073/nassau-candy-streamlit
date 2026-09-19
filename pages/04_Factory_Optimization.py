import streamlit as st
from services.scenario_service import scenario_predictions, factories
from components.filters import scenario_filters
from components.warnings import show_global_warnings

st.title('Factory Optimization Simulator')
show_global_warnings()

product, region, ship_mode = scenario_filters()
year = st.selectbox('Scenario order year', [2024, 2025], index=1)
month = st.slider('Scenario order month', 1, 12, 6)

out, current, fallback = scenario_predictions(product, region, ship_mode, year, month)
st.write(f'**Current factory:** {current}')

if fallback:
    st.warning(
        'The packaged binary model could not be loaded in this deployment. '
        'The app is using a historical product/region/ship-mode baseline proxy. '
        'Factory-specific effects are intentionally not invented because factory is confounded with product in the source data.'
    )
else:
    st.info('Factory alternatives below are model-based counterfactual proxies, not observed factory effects.')

st.dataframe(out, use_container_width=True, hide_index=True)
st.markdown('### Factory coordinates')
st.dataframe(factories(), use_container_width=True, hide_index=True)
