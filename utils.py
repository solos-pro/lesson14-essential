import json
import sqlite3

def get_movie_by_title(title):
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
    data_raw =cur.fetchone()

    data = {
        "title": data_raw[0],
        "country": data_raw[1],
        "release_year": data_raw[2],
        "genre": data_raw[3],
        "description": data_raw[4]
        }
    con.close()

    return data

print(get_movie_by_title("1994"))

def get_all_movies_between_years(year1, year2):

    pass


def get_all_movies_by_genre(genre):

    pass


def get_all_movies_by_rating(rating):

    pass


def get_actors_company(first, second):

    pass


def filter_movies(movie_type, year, genre):

    pass

