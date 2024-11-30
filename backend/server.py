from fastapi import FastAPI,HTTPException
from datetime import date
import db_helper
from pydantic import BaseModel
from typing import List
app= FastAPI()

class expense(BaseModel):
   # expense_date: date
    amount: float
    category: str
    notes: str
class analytics(BaseModel):
     start_date:date
     end_date:date
@app.get("/expenses/{expense_date}",response_model=List[expense])
def get_expenses(expense_date:date):
    expenses=db_helper.fetch_expenses_date(expense_date)
    return expenses
@app.post("/expenses/{expense_date}")
def add_update_expnese(expense_date:date,expenses:List[expense]):
    db_helper.delete_expense(expense_date)
    for expense in expenses:
      db_helper.insert_expenses(expense_date,expense.amount,expense.category,expense.notes)
    return {'message':'expenses upadted successfull'}
@app.post("/analytics/")
def fetch_expense_summary(daterange:analytics):
    data=db_helper.fetch_expenses_in_date_range(daterange.start_date,daterange.end_date)
    if data==None:
        raise HTTPException(status_code=500,detail="No data available")
    breakdown={}
    Grand_total=sum(i['total'] for i in data) # summing up all total to calculate percentage
    for i in data:
        percentage=(i['total']/Grand_total)*100 if Grand_total !=0 else 0 # handling devide by 0 exception
        breakdown[i['category']]={
            "total": i['total'],
            "percentage":round(percentage,2)
        }
    return breakdown
@app.get("/analytics_monthly/")
def fetch_expenses_month():
    expenses=db_helper.fetch_expenses_by_month()
    return expenses
