import streamlit as st
from services.analysis_service import priority_segments
from components.warnings import show_global_warnings
st.title('Recommendations'); show_global_warnings()
df=priority_segments().copy()
speed=st.slider('Lead-time priority',0.0,1.0,0.6,0.05)
risk=st.slider('Risk priority',0.0,1.0,0.2,0.05)
profit=1-speed-risk
if profit < 0: st.error('Lead-time and risk weights sum above 1. Reduce one before using the ranking.'); st.stop()
df['speed_score']=df['lead_time_mean'].rank(pct=True,ascending=False)
df['profit_exposure_score']=df['priority_exposure'].rank(pct=True)
df['risk_score']=1-df['gross_margin_pct'].rank(pct=True)
df['recommendation_score']=speed*df['speed_score']+profit*df['profit_exposure_score']+risk*df['risk_score']
st.dataframe(df.sort_values('recommendation_score',ascending=False).head(20),use_container_width=True,hide_index=True)
