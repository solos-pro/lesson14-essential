import sqlite3

con = sqlite3.connect("netflix.db")
cur = con.cursor()
sqlite_query = """
    SELECT COUNT(title)  FROM netflix
    WHERE country LIKE '%India%'

"""
cur.execute(sqlite_query)
executed_query = cur.fetchall()

print(executed_query)
