import  streamlit as st
from add_update_UI import add_update_tab
from analytic_UI import analytics_tab
from Monthly_analytics_ui import monthly_expense
st.title('Expense Management Tracker')
tab1,tab2,tab3=st.tabs(['Add/Update','Analytics','Monthly_analytics'])
with tab1:
    add_update_tab()
with tab2:
    analytics_tab()
with tab3:
    monthly_expense()



