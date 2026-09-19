import streamlit as st
from services.analysis_service import region_summary, product_summary
from components.charts import bar
from components.warnings import show_global_warnings
st.title('Overview'); show_global_warnings()
r=region_summary(); p=product_summary()
st.plotly_chart(bar(r.sort_values('sales',ascending=False),'Region','sales','Historical Sales by Region'),use_container_width=True)
st.plotly_chart(bar(p.sort_values('gross_profit',ascending=False).head(10),'Product Name','gross_profit','Top Products by Historical Gross Profit'),use_container_width=True)
st.dataframe(r,use_container_width=True,hide_index=True)
