import jsonify
import pprint
import sqlite3

def get_movie_by_title(title):
    """
    #1  Returns movie by title.
    http://localhost:5000/movies/1994
    """
    con = sqlite3.connect("netflix.db")
    sqlite_query = f"""
        SELECT `title`, `country`, `release_year`, `listed_in`, `description`
        FROM netflix
        WHERE title = {title} 
        ORDER BY `release_year`
        LIMIT 1
        """
    cur = con.cursor()
    cur.execute(sqlite_query)
    data_raw = cur.fetchone()

    data = {
        "title": data_raw[0],
        "country": data_raw[1],
        "release_year": data_raw[2],
        "genre": data_raw[3],
        "description": data_raw[4]
        }
    con.close()

    return data


def get_all_movies_between_years(year1, year2):
    """
    #2  Returns movies from <year> to <year> inclusive.
    http://localhost:5000/years/2000/to/2011
    """
    con = sqlite3.connect("netflix.db")
    sqlite_query = f"""
        SELECT `title`, `country`, `release_year`, `listed_in`, `description`
        FROM netflix
        WHERE `release_year` BETWEEN {year1} AND {year2} 
        LIMIT 100
        """
    cur = con.cursor()
    cur.execute(sqlite_query)

    data = []
    for row in cur.fetchall():
        movie = {
            "title": row[0],
            "country": row[1],
            "release_year": row[2],
            "genre": row[3],
            "description": row[4]
            }
        data.append(movie)

    con.close()
    return data
# print(get_all_movies_between_years(2020, 2021))

def get_all_movies_by_rating(age_group):
    """
    #3  Filter by age permission.
    http://localhost:5000/rating/children
    """
    if age_group == 'children':
        sqlite_query = """
            SELECT `title`, `rating`, `description`
            FROM netflix
            WHERE `rating` IN ('G')
            ORDER BY 'rating'
            LIMIT 5
            """
    if age_group == 'family':
        sqlite_query = """
            SELECT `title`, `rating`, `description`
            FROM netflix
            WHERE `rating` IN ('PG', 'PG-13')
            ORDER BY 'rating'
            LIMIT 5
            """
    if age_group == 'adult':
        sqlite_query = """
            SELECT `title`, `rating`, `description`
            FROM netflix
            WHERE `rating` IN ('R', 'NC-17')
            ORDER BY 'rating'
            LIMIT 5
            """

    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    cur.execute(sqlite_query)

    data = []
    for row in cur.fetchall():
        movie = {
            "title": row[0],
            "rating": row[1],
            "description": row[2]
            }
        data.append(movie)

    con.close()
    return data

    pass


def get_all_movies_by_genre(genre):
    """
     #4 A function returns 10 newest movies ordered by <genre> (Drama,
     Horror, Crime, Adventure, Anime, ...).
     http://localhost:5000/genre/Crime
     """
    con = sqlite3.connect("netflix.db")
    sqlite_query = f"""
        SELECT `title`, `description`, `listed_in`
        FROM netflix
        WHERE `listed_in` LIKE '%{genre}%'
        LIMIT 10
        """
    cur = con.cursor()
    cur.execute(sqlite_query)

    data = []
    for row in cur.fetchall():
        movie = {
            "title": row[0],
            "description": row[1],
            "genre": row[2]
            }
        data.append(movie)

    con.close()
    return data


def get_actors_company(first, second):
    """
    #5  A function returns a list of colleagues of two actors who play with them twice or more times.
    http://localhost:5000/collab/Jack%20Black/Dustin%20Hoffman
    """
    con = sqlite3.connect("netflix.db")
    sqlite_query = f"""
        SELECT GROUP_CONCAT(`cast`, ',') as cast
        FROM netflix
        WHERE `cast` LIKE '%{first}%' AND `cast` LIKE '%{second}%'
        LIMIT 100
        """
    cur = con.cursor()
    cur.execute(sqlite_query)
    data_raw = cur.fetchone()
    con.close()

    actors_list = data_raw[0].split(', ')
    actors_list_unique = set(actors_list)

    suitable_actor = []
    for actor in actors_list_unique:
        if actor != first and actor != second and actors_list.count(actor) >= 2:
            suitable_actor.append(actor)
    return suitable_actor


def filter_movies(movie_type, year, genre):
    """
    #6  A function returns a list of movies depend on type, year, genre.
    http://localhost:5000/filter/Movie/2020/Drama
    """
    con = sqlite3.connect("netflix.db")
    sqlite_query = f"""
    SELECT `title`, `rating`, `description`, `listed_in`, `release_year`
    FROM netflix
    WHERE `type`='{movie_type}'
    AND `release_year`={year}
    AND `listed_in` LIKE '%{genre}%'
    LIMIT 10
    """
    cur = con.cursor()
    cur.execute(sqlite_query)

    data = []
    for row in cur.fetchall():
        movie = {
            "title": row[0],
            "description": row[2],
            "genre": row[3]
            }
        data.append(movie)

    con.close()
    return data

