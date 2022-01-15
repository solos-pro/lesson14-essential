import jsonify, json
from flask import Flask, render_template, request
from utils import get_movie_by_title, get_all_movies_between_years

app = Flask(__name__)


@app.route('/movies/<title>', )
def by_title(title):
    movie = get_movie_by_title(title)
    return json.dumps(movie)


@app.route('/years/<int:beginning>/to/<int:ending>', )
def by_years(beginning, ending):
    movie = get_all_movies_between_years(beginning, ending)
    print(movie)
    return json.dumps(movie)


app.run(debug=True)

# print(get_movie_by_title('1994'))
