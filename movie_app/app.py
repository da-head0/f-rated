from flask import Flask, request, Response
from flask_mongoengine import MongoEngine
from database.db import initialize_db
from database.models import Movie
import os
import json

app = Flask(__name__)


DB_URI = "mongodb+srv://aimb:mimomimo@cluster0.xc44g.mongodb.net/frated?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_URI
db = MongoEngine(app)

# initialize database
@app.route('/movies')
def get_movies():
    movies = Movie.objects().to_json() # to_json() 해야 보임
    #mov_title = movies[0]['Title']
    return Response(movies, mimetype="application/json", status=200)

@app.route('/movies', methods=['POST'])
def add_movie():
    body = request.get_json()
    movie =  Movie(**body).save()
    id = movie.id
    return {'id': str(id)}, 200

@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200

@app.route('/movies/<id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.objects.get(id=id).delete()
    return '', 200

@app.route('/movies/<id>')
def get_movie(id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)

if __name__ == '__main__':
    app.run()