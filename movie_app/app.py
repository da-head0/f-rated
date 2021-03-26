from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from flask_mongoengine import MongoEngine
from resources.routes import initialize_routes
import os


app = Flask(__name__)

# create API
api = Api(app)

DB_URI = "mongodb+srv://aimb:mimomimo@cluster0.xc44g.mongodb.net/frated?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_URI
#db = MongoEngine(app)
initialize_db(app)
initialize_routes(api) # initialize_routes(api)

if __name__ == '__main__':
    app.run()