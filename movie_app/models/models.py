from database.db import *
from database.get_keywords import get_keyword, get_rottentomatoes
#from bson.objectid import ObjectId

# db랑 연동되면 Movie -> movie 라는 collection이 만들어진다.

# class ID(db.EmbeddedDocument):
#     oid = db.StringField()

# class Ratings(db.EmbeddedDocument):
#     # source = db.StringField()
#     # value = db.StringField()
#     #ratings = db.StringField()
#     source = db.StringField()
#     value = db.StringField()
#     source = db.StringField()
#     field3 = db.StringField()
#     field2 = db.StringField()
#     field3 = db.StringField()
#     field2 = db.StringField()
#     field3 = db.StringField()

# 실제 json 파일이랑 대문자를 같게 해야 한다...
class Movie(db.Document):
    imdbID = db.StringField() # primary key?
    Title = db.StringField()
    Year = db.IntField()
    Rated = db.StringField() # 관람등급
    Released = db.StringField()
    Runtime = db.StringField() 
    Genre = db.StringField()
    Genre1 = db.StringField()
    Director = db.StringField()
    Writer = db.StringField()
    Actors = db.StringField()
    Plot = db.StringField()
    Language = db.StringField()
    Country = db.StringField()
    Awards = db.StringField()
    Poster = db.StringField()
    Ratings = db.ListField(db.DictField()) #db.EmbeddedDocumentListField(Ratings)
    Metascore = db.StringField()
    RottenTomatoes = db.StringField()
    imdbRating = db.FloatField()
    imdbVotes = db.StringField()
    BoxOffice = db.StringField()
    Production = db.StringField()
    keywords = db.ListField()
    meta = {'strict': False} #ignoring this error when having extra fields while data loading

    def __repr__(self):
        return f"{self.Title} \n 키워드: {self.keywords}"
#db.movie.dropIndex() # 유니크 키가 중복될 때 터미널 창에서 실행해볼 것...

# 칼럼 아이디를 대문자로 바꿔야 Postman에서 동작됐는데 그러면 NotUniqueError가 일어나 다 소문자로 바꿔봄...