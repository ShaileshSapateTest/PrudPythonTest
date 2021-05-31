import numpy as np
import pandas as pd
import sqlite3

# Establish DB connection
conn = sqlite3.connect('C:\PythonTest\Prudential_Data.db')

sqlite_query = """
WITH FT_CTE AS (
  SELECT [customer id] AS Customer_Id,Max([policy_value_snapshot]) - Min([policy_value_snapshot]) As PolicyVaulueDifference
  FROM Fund_Table 
  Where [policy_value_snapshot] <> 'NULL'
  Group By [customer id]
  Order by [Date]
)
SELECT Customer_Id,max(PolicyVaulueDifference) as customerwithBiggestDiff
from FT_CTE
WHERE PolicyVaulueDifference = (SELECT max(PolicyVaulueDifference) from FT_CTE)
"""
pd1 = pd.read_sql(sqlite_query, conn)

print (pd1)