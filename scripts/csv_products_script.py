import pandas
import sqlite3

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
c.execute('''CREATE TABLE products (products_id int, name text)''')

df = pandas.read_csv('scripts/static/products.csv', sep='encoding')
df.to_sql(df, conn, if_exists='append', index=False)
