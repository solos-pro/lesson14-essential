import sqlite3, jsonify
from flask import Flask, render_template, request
from utils import *

@app.route('/movies/<title>'):
def index_func(title):
    movie = get_movie_by_title(title)
    print(movie)
