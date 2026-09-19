import streamlit as st
from services.analysis_service import audit, product_summary
from components.cards import metric_row
from components.warnings import show_global_warnings

st.set_page_config(page_title='Nassau Candy Optimization', page_icon='🍫', layout='wide')
st.title('Nassau Candy Distributor')
st.subheader('Factory Reallocation & Shipping Optimization Decision Support')
show_global_warnings()

a=audit(); p=product_summary()
metric_row([
    ('Rows',format(a['rows'],',')),
    ('Orders',format(a['unique_order_ids'],',')),
    ('Products',str(a['unique_products'])),
    ('Missing cells',format(a['missing_cells'],','))
])

st.markdown('### What this application does')
st.write('The application combines historical aggregates with a versioned predictive model to explore factory scenarios. Historical, predicted and simulated values are kept distinct.')

st.markdown('### Historical business view')
metric_row([
    ('Sales','$' + format(p['sales'].sum(),',.2f')),
    ('Gross profit','$' + format(p['gross_profit'].sum(),',.2f')),
    ('Units',format(p['units'].sum(),',.0f')),
    ('Median recorded lead time',format(a['lead_time_median'],',.0f') + ' days')
])
st.caption('Use the pages in the sidebar for data quality, model performance, factory optimization, what-if analysis and recommendations.')
