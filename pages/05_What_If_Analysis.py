import streamlit as st
import plotly.express as px
from services.scenario_service import scenario_predictions
from components.filters import scenario_filters
from components.warnings import show_global_warnings
st.title('What-If Analysis'); show_global_warnings()
product,region,ship_mode=scenario_filters()
year=st.selectbox('Scenario year',[2024,2025],index=1)
month=st.slider('Scenario month',1,12,6)
priority=st.slider('Optimization priority — speed vs profit',0.0,1.0,0.7,0.05)
out,current=scenario_predictions(product,region,ship_mode,year,month)
out['priority_score']=priority*out['simulated_improvement_days'].clip(lower=0)
fig=px.bar(out.sort_values('predicted_recorded_lead_time_days'),x='factory',y='predicted_recorded_lead_time_days',title='Predicted recorded lead time by hypothetical factory')
st.plotly_chart(fig,use_container_width=True)
selected=out.sort_values('predicted_recorded_lead_time_days').iloc[0]
baseline=out.loc[out['current_factory'],'predicted_recorded_lead_time_days'].iloc[0]
st.write(f'Current predicted baseline: **{baseline:.1f} days**')
st.write(f"Lowest model-based scenario: **{selected['predicted_recorded_lead_time_days']:.1f} days** at **{selected['factory']}**")
st.caption('This is a model-based scenario, not evidence of operational feasibility, incremental profit or causal factory effects.')
