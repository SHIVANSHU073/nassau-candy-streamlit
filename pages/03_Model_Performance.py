import streamlit as st
from services.analysis_service import model_metrics
from components.warnings import show_global_warnings
st.title('Model Performance'); show_global_warnings()
metrics=model_metrics()
st.dataframe(metrics,use_container_width=True,hide_index=True)
st.caption('Metrics are from a chronological 80/20 validation split and predict recorded lead-time days, not validated physical transit time.')
best=metrics.sort_values('RMSE').iloc[0]
st.info(f"Lowest RMSE among tested models: {best['model']} (RMSE {best['RMSE']:.2f}, R² {best['R2']:.3f}). Predictive explanatory power is weak.")
