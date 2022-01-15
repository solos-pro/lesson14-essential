import sqlite3, jsonify
from flask import Flask, render_template, request
from utils import get_movie_by_title

app = Flask(__name__)


@app.route('/movies/<title>', )
def index_func(title):
    movie = get_movie_by_title(title)
    return movie

app.run(debug=True)

# print(get_movie_by_title('1994'))
