from matplotlib.legend import Legend
import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import plotly.express as px

# Establish DB connection
conn = sqlite3.connect('C:\PythonTest\Prudential_Data.db')

sqlite_query = """
SELECT CASE 
		WHEN ct.age BETWEEN 1 and 20 then '1-20'
       	WHEN ct.age BETWEEN 21 and 30 then '21-30'
        WHEN ct.age BETWEEN 31 and 40 then '31-40'
        WHEN ct.age BETWEEN 41 and 50 then '41-50'
        WHEN ct.age BETWEEN 51 and 60 then '51-60'
        WHEN ct.age BETWEEN 61 and 70 then '61-70'
        WHEN ct.age BETWEEN 71 and 80 then '71-80'
        WHEN ct.age BETWEEN 81 and 90 then '81-90'
        WHEN ct.age BETWEEN 91 and 100 then '91-100'
       END as 'Age Range',
ct.[gender] as Gender,round(Avg(pt.[Policy Value]),2) AS 'Avg Policy Value'
FROM Customer_Table ct join Policy_Table pt on ct.[customer id] = pt.[customer id]
Group by CASE 
		WHEN ct.age BETWEEN 1 and 20 then '1-20'
       	WHEN ct.age BETWEEN 21 and 30 then '21-30'
        WHEN ct.age BETWEEN 31 and 40 then '31-40'
        WHEN ct.age BETWEEN 41 and 50 then '41-50'
        WHEN ct.age BETWEEN 51 and 60 then '51-60'
        WHEN ct.age BETWEEN 61 and 70 then '61-70'
        WHEN ct.age BETWEEN 71 and 80 then '71-80'
        WHEN ct.age BETWEEN 81 and 90 then '81-90'
        WHEN ct.age BETWEEN 91 and 100 then '91-100'
       END,ct.[gender]
"""
pd1 = pd.read_sql(sqlite_query, conn)

#ns.catplot(data=pd1, kind="bar", x="Age Range", y="Avg Policy Value", hue="Gender")
x="Age Range"
y="Avg Policy Value"
color_discrete_map1 = {'Male': 'rgb(131, 153, 214)','Female': 'rgb(206, 150, 205)'}

fig = px.bar(pd1, x="Age Range", y="Avg Policy Value", color = 'Gender',
hover_data=["Age Range", "Gender","Avg Policy Value"], 
labels={"Avg Policy Value":'Avg Policy Value'}, height=500,
color_discrete_map = color_discrete_map1)

fig.update_layout(barmode='group',
    title = "Policy Value by Age Range and Gender",
    bargap =  0.15,
    bargroupgap= 0.1,
    legend_title_text ="",
    legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1))

fig.show()