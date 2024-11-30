import os
import sys
file=r"C:\\Users\\prasad bolgss\\PycharmProjects\\Expense_Tracker\\backend\\"
project_root=os.path.abspath(os.path.join(file,'..'))
print(project_root)
sys.path.insert(0,project_root)
print(sys.path)