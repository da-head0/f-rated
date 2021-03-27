from flask import Flask
from database.db import initialize_db
#from flask_restful import Api
from flask_mongoengine import MongoEngine
#from routes.routes import initialize_routes
#import os


app = Flask(__name__)

# # create API
# api = Api(app)

DB_URI = "mongodb+srv://aimb:mimomimo@cluster0.xc44g.mongodb.net/frated?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = DB_URI
#db = MongoEngine(app)

initialize_db(app)
#initialize_routes(api) 

from routes import (main_route, user_route)
from resources.movie import *

app.register_blueprint(main_route.bp)
app.register_blueprint(movies)
app.register_blueprint(user_route.bp) #, url_prefix='/api')

if __name__ == '__main__':
    app.run()