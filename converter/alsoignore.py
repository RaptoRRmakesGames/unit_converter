import sqlite3

conn = sqlite3.connect("stuff.db")

c = conn.cursor()

collumn = input("Enter collumn --> ")


c.execute(
"""UPDATE foods
SET column1 = value1, column2 = value2...., columnN = valueN
WHERE name='Egg White' ;""")