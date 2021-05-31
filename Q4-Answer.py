import numpy as np
import pandas as pd
import sqlite3
import re

# Establish DB connection
conn = sqlite3.connect('C:\PythonTest\Prudential_Data.db')

Customer_Table = pd.read_sql('SELECT [Customer ID],[Email] FROM Customer_Table', conn)

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
 
def check(email):
 
    if(email != None and re.search(regex, email)):
        return True
 
    else:
        return False

Customer_Table['is_valid_email'] = Customer_Table['Email'].apply(lambda x:check(x))

print (Customer_Table)