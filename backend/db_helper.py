import mysql.connector
from contextlib import contextmanager
from logger_setup import setup_logger



logger=setup_logger('db_helper')




@contextmanager
def get_db_connection(commit=False):
    connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='new_password',
        database='expense_manager'
    )
    if connection.is_connected():
        print('connection successfull')
    else:
        print('error')
    cursor=connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()


def fetch_records():
    logger.info('fetch records function called')
    with get_db_connection() as cursor:
        cursor.execute('select * from Expenses')
        expenses=cursor.fetchall()
        for expense in expenses:
            print(expense)
def fetch_expenses_date(expense_date):
    logger.info(f'fetch_expenses_date function called with expense date:{expense_date}')

    with get_db_connection() as cursor:
        cursor.execute('select * from Expenses where Expense_date=%s',(expense_date,))
        expenses=cursor.fetchall()
        for expense in expenses:
            print(expense)
        return expenses

def insert_expenses(expense_date,amount,category,notes):
    logger.info(f'insert_expenses function called with expense date:{expense_date}')

    with get_db_connection(commit=True) as cursor:
        cursor.execute('INSERT INTO expenses (expense_date,amount,category,notes) VALUES(%s,%s,%s,%s)',
                       (expense_date,amount,category,notes))
def delete_expense(expense_date):
    logger.info(f'delete_expense function called with expense date:{expense_date}')

    with get_db_connection(commit=True) as cursor:
        cursor.execute('DELETE from Expenses where expense_date=%s',(expense_date,))
def fetch_expenses_in_date_range(start_date,end_date):
    logger.info(f'getting expense summary from {start_date} to {end_date}')
    with get_db_connection() as cursor:
            query = "SELECT category, SUM(amount) AS total FROM expenses WHERE expense_date BETWEEN %s AND %s GROUP BY category;"
            cursor.execute(query, (start_date, end_date))
            data = cursor.fetchall()
            return data
def fetch_expenses_by_month():
    logger.info(f'getting  month wise expense summary ')
    with get_db_connection() as cursor:
            query = "select sum(amount)as total,monthname(expense_date) as Exp_month from expenses  where expense_date group by Exp_month;"
            cursor.execute(query)
            data = cursor.fetchall()
            return data

if __name__=="__main__":
    """fetch_records()
    insert_expenses('24-08-20','30','Food','Panipuri')"""
    fetch_expenses_date('24-08-20')
    fetch_expenses_in_date_range('24-08-1','24-08-20')

