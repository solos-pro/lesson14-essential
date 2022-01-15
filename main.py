import jsonify, json
from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)


@app.route('/movies/<title>', )
def by_title(title):
    movie = get_movie_by_title(title)
    return json.dumps(movie)


@app.route('/years/<int:beginning>/to/<int:ending>', )
def by_years(beginning, ending):
    movies = get_all_movies_between_years(beginning, ending)
    return json.dumps(movies)


@app.route('/rating/<age>', )
def by_rating(age):
    movies = get_all_movies_by_rating(age)
    return json.dumps(movies)


app.run(debug=True)

# print(get_movie_by_title('1994'))
