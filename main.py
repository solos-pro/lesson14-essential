import sqlite3
# import Flask

con = sqlite3.connect("netflix.db")
sqlite_query = "SELECT * FROM netflix LIMIT 1"
cur = con.cursor()
data = cur.execute(sqlite_query)
print(data.fetchone())

#1
"""
SELECT `title`, `country`, `release_year`, `listed_in`, `description`
FROM netflix
WHERE title = "1994" 
ORDER BY `release_year`
LIMIT 1
"""
#2
"""
SELECT `title`, `country`, `release_year`, `listed_in`, `description`
FROM netflix
WHERE `release_year` BETWEEN 2020 AND 2021 
LIMIT 100
"""
"""
SELECT `title`, `rating`, `description`
FROM netflix
WHERE `rating` IN ("G", "PG", "PG-13")  
"""
"""
SELECT `title`, `rating`, `description`, `listed_in`
FROM netflix
WHERE `listed_in` LIKE "%Drama%"
LIMIT 100
"""
"""
SELECT GROUP_CONCAT(`cast`, ",") as cast
FROM netflix
WHERE `cast` LIKE "%Jack Black%" AND `cast` LIKE "%Dustin Hoffman%"
LIMIT 100
"""
"""
SELECT `title`, `rating`, `description`, `listed_in`, `release_year`
FROM netflix
WHERE `type`="Movie"
AND `release_year`=2020
AND `listed_in` LIKE "%Drama%"
LIMIT 100
"""
con = sqlite3.connect("netflix.db")
cur = con.cursor()
sqlite_query = """
    SELECT COUNT(title)  FROM netflix
    WHERE country LIKE '%India%'

"""
cur.execute(sqlite_query)
executed_query = cur.fetchall()

print(executed_query)
