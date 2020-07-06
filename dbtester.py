# dbtester.py

import pandas as pd
import sqlite3


conn = sqlite3.connect('todo.db')
df = pd.read_sql_query("SELECT * from Todo", conn)

print(df)