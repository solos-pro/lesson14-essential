import sqlite3
# import Flask

con = sqlite3.connect("netflix.db")
sqlite_query = "SELECT * FROM netflix LIMIT 1"
cur = con.cursor()
data = cur.execute(sqlite_query)
print(data.fetchone())


con = sqlite3.connect("netflix.db")
cur = con.cursor()
sqlite_query = """
    SELECT COUNT(title)  FROM netflix
    WHERE country LIKE '%India%'

"""
cur.execute(sqlite_query)
executed_query = cur.fetchall()

print(executed_query)
