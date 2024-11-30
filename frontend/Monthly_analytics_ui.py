import  streamlit as st
from datetime import datetime
import requests
import pandas as pd
API_URL='http://localhost:8000'
def monthly_expense():

    response=requests.get(f'{API_URL}/analytics_monthly')
    if response.status_code==200:
        existing_expenses=response.json()

        #st.write(data_list)

        df=pd.DataFrame(existing_expenses)
        st.table(df)
        df_sorted=df.sort_values(by='Exp_month',ascending=False)
        st.title("Expense breakdown by month")
        st.bar_chart(df_sorted.set_index('Exp_month')['total'])


    else:
        st.error('Failed to retrive existing expenses')
        existing_expenses=[]