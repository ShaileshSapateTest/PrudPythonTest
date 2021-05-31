import numpy as np
import pandas as pd
import sqlite3

# Establish DB connection
conn = sqlite3.connect('C:\PythonTest\Prudential_Data.db')

sqlite_query = """
SELECT [Product Name],Avg([Policy Value])
from Policy_Table
Group By [Product Name]
"""

pd.read_sql(sqlite_query, conn)

print (pd.read_sql(sqlite_query, conn))