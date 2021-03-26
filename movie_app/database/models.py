from .db import db

# db랑 연동되면 Movie -> movie 라는 collection이 만들어진다.

class Ratings(db.EmbeddedDocument):
    Source = db.StringField()
    Value = db.StringField()
    # InternetMovieDatabase = db.StringField()
    # RottenTomatoes = db.StringField()
    # Metacritic = db.StringField()

# 실제 json 파일이랑 대문자를 같게 해야 한다...
class Movie(db.Document):
    Title = db.StringField()
    Year = db.IntField()
    Rated = db.StringField() # 관람등급
    Released = db.StringField() # datetime으로 바꿀 수 있을듯
    Runtime = db.IntField() # int로 바꿀 수 있을듯
    Genre = db.StringField() # 리스트?
    Genre1 = db.StringField()
    Director = db.StringField()
    Writer = db.StringField()
    Actors = db.StringField()
    Plot = db.StringField()
    Language = db.StringField()
    Country = db.StringField()
    Awards = db.StringField()
    Poster = db.StringField()
    #Ratings = db.StringField()
    Ratings = db.EmbeddedDocumentListField(Ratings) # source는 string, value는 int 혹은 float
    #Metascore = db.StringField() #["Ratings"][1]["Value"]
    Metascore = db.IntField()
    RottenTomatoes = db.StringField()
    imdbRating = db.FloatField()
    imdbVotes = db.IntField()
    imdbID = db.StringField(unique=True) # primary key?
    BoxOffice = db.IntField()
    Production = db.StringField()
    meta = {'strict': False} #ignoring this error when having extra fields while data loading
