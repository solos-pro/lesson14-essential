""""""
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
#3
"""
SELECT `title`, `rating`, `description`
FROM netflix
WHERE `rating` IN ("G", "PG", "PG-13")
ORDER BY 'rating' 
"""
#4
"""
SELECT `title`, `rating`, `description`, `listed_in`
FROM netflix
WHERE `listed_in` LIKE "%Drama%"
LIMIT 100
"""
#5
"""
SELECT GROUP_CONCAT(`cast`, ',') as cast
FROM netflix
WHERE `cast` LIKE '%Jack Black%' AND `cast` LIKE '%Dustin Hoffman%'
LIMIT 100
"""
#6
"""
SELECT `title`, `rating`, `description`, `listed_in`, `release_year`
FROM netflix
WHERE `type`='Movie'
AND `release_year`=2020
AND `listed_in` LIKE '%Drama%'
LIMIT 100
"""