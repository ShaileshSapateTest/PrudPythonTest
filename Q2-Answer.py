import numpy as np
import pandas as pd
import sqlite3

# Establish DB connection
conn = sqlite3.connect('C:\PythonTest\Prudential_Data.db')

sqlite_query = """
SELECT[Customer ID],[Product Name],[Policy Start Date]
from Policy_Table a
Where [Policy Start Date] Between '2017-01-01' and '2017-03-31'
and [Customer ID] IN (SELECT[Customer ID]
                        from Policy_Table b
                        Where [Product Name] = 'NHS PENSION'
                        AND a.[Policy Start Date] > b.[Policy Start Date])
"""
pd1 = pd.read_sql(sqlite_query, conn)

print (pd1)