import jsonify, json, flask
from flask import Flask, render_template, request, jsonify
from utils import *

'''
    #1
    Returns movie by title.
    http://localhost:5000/movies/1994

    #2  Returns movies from <year> to <year> inclusive.
    http://localhost:5000/years/2000/to/2011

    #3  Filter by age permission.
    http://localhost:5000/rating/children

     #4 A function returns 10 newest movies ordered by <genre> (Drama,
     Horror, Crime, Adventure, Anime, ...).
     http://localhost:5000/genre/Crime

    #5  A function returns a list of colleagues of two actors who play with them twice or more times.
    http://localhost:5000/collab/Jack%20Black/Dustin%20Hoffman

    #6  A function returns a list of movies depend on type, year, genre.
    http://localhost:5000/filter/Movie/2020/Drama

'''

app = Flask(__name__)


@app.route('/movies/<title>', )
def by_title(title):
    movie = get_movie_by_title(title)
    return flask.jsonify(movie)


@app.route('/years/<int:beginning>/to/<int:ending>', )
def by_years(beginning, ending):
    movies = get_all_movies_between_years(beginning, ending)
    return flask.jsonify(movies)


@app.route('/rating/<age>', )
def by_rating(age):
    movies = get_all_movies_by_rating(age)
    return flask.jsonify(movies)


@app.route('/genre/<genre>', )
def by_genre(genre):
    movies = get_all_movies_by_genre(genre)
    return flask.jsonify(movies)


@app.route('/collab/<actor1>/<actor2>', )
def actors_collab(actor1, actor2):
    actors = get_actors_company(actor1, actor2)
    return flask.jsonify(actors)


@app.route('/filter/<movie_type>/<int:year>/<genre>', )
def filter_movies_func(movie_type, year, genre):
    movies = filter_movies(movie_type, year, genre)
    return flask.jsonify(movies)


app.run(debug=True)

