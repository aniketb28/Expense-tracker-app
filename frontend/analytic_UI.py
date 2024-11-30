import  streamlit as st
from datetime import datetime
import requests
import pandas as pd
API_URL='http://localhost:8000'
def analytics_tab():
    col1,col2=st.columns(2)
    with col1:
        start_date=st.date_input("Start_date",datetime(2024,8,1))
    with col2:
        end_date = st.date_input("End_date", datetime(2024,8,20))
    payload={
             'start_date': start_date.strftime('%Y-%m-%d'),
              'end_date':end_date.strftime('%Y-%m-%d')
    }
    if st.button("Get analytics"):
        response=requests.post(f'{API_URL}/analytics',json=payload)
        result=response.json()
        data={
            'Category':list(result.keys()),
            'Total':[result[category]["total"] for category in result],
            'Percentage':[result[category]["percentage"] for category in result]
        }
        df=pd.DataFrame(data)
        #st.table(df)
        df_sorted=df.sort_values(by='Percentage',ascending=False)
        st.title("Expense breakdown by category")
        st.bar_chart(df_sorted.set_index('Category')['Percentage'])