from flask import Flask, render_template
from flask_mongoengine import MongoEngine
from mongoengine import connect
from flask_migrate import Migrate
from pymongo import MongoClient
import csv
import os

db = MongoEngine()
migrate = Migrate()
client = MongoClient()

def create_app():
    app = Flask(__name__)
    app.config['MONGODB_DB'] = 'frated'
    app.config['MONGODB_COLLECTION'] = 'mov'
    app.config['MONGODB_HOST'] = 'cluster0.xc44g.mongodb.net'
    #app.config['MONGODB_PORT'] = 12345
    app.config['MONGODB_USERNAME'] = 'aimb'
    app.config['MONGODB_PASSWORD'] = 'aibootcamp'
    app.config['MONGOALCHEMY_SERVER_AUTH'] = False
    
    db.init_app(app)
    migrate.init_app(app, db)

    # from flask_app import main_routes
    # app.register_blueprint(main_routes.bp)
    movies = [
        {
            "Title": "Thelma & Louise",
            "Year": "1991",
            "Rated": "R",
            "Released": "24 May 1991",
            "Runtime": "130 min",
            "Genre": "Adventure, Crime, Drama",
            "Director": "Ridley Scott",
            "Writer": "Callie Khouri",
            "Actors": "Susan Sarandon, Geena Davis, Harvey Keitel, Michael Madsen",
            "Plot": "Two best friends set out on an adventure, but it soon turns around to a terrifying escape from being hunted by the police, as these two girls escape for the crimes they committed.",
            "Language": "English",
            "Country": "USA, UK, France",
            "Awards": "Won 1 Oscar. Another 23 wins & 50 nominations.",
            "Poster": "https://m.media-amazon.com/images/M/MV5BMjIxNDgzMDE2MF5BMl5BanBnXkFtZTcwNzY5NTk1NA@@._V1_SX300.jpg",
            "Ratings": [
                {
                "Source": "Internet Movie Database",
                "Value": "7.5/10"
                },
                {
                "Source": "Rotten Tomatoes",
                "Value": "84%"
                },
                {
                "Source": "Metacritic",
                "Value": "88/100"
                }
            ],
            "Metascore": "88",
            "imdbRating": "7.5",
            "imdbVotes": "137,893",
            "imdbID": "tt0103074",
            "Type": "movie",
            "DVD": "18 Jun 2016",
            "BoxOffice": "$45,360,915",
            "Production": "Metro Goldwyn Mayer",
            "Website": "N/A",
            "Response": "True"
            }
            ]

    @app.route('/')
    def hello():
        return jsonify(movies)

    return app

if __name__  == "__main__":
    app = create_app()
    app.run(debug=True)