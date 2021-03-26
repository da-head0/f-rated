from .db import db
#from bson.objectid import ObjectId

# db랑 연동되면 Movie -> movie 라는 collection이 만들어진다.

# class ID(db.EmbeddedDocument):
#     oid = db.StringField()

class Ratings(db.EmbeddedDocument):
    source = db.StringField()
    value = db.StringField()

# 실제 json 파일이랑 대문자를 같게 해야 한다...
class Movie(db.Document):
    #_id = db.EmbeddedDocumentListField(ID)
    title = db.StringField()
    year = db.IntField()
    rated = db.StringField() # 관람등급
    released = db.StringField() # datetime으로 바꿀 수 있을듯
    runtime = db.IntField() 
    genre = db.StringField()
    genre1 = db.StringField()
    director = db.StringField()
    writer = db.StringField()
    actors = db.StringField()
    plot = db.StringField()
    language = db.StringField()
    country = db.StringField()
    awards = db.StringField()
    poster = db.StringField()
    #Ratings = db.StringField()
    ratings = db.EmbeddedDocumentListField(Ratings) 
    metascore = db.StringField()
    rottentomatoes = db.StringField()
    imdbrating = db.FloatField()
    imdbvotes = db.IntField()
    imdbid = db.StringField() # primary key?
    boxOffice = db.IntField()
    production = db.StringField()
    meta = {'strict': False} #ignoring this error when having extra fields while data loading

    def __repr__(self):
        return f"{self.title}"
#db.movie.dropIndex() # 유니크 키가 중복될 때 터미널 창에서 실행해볼 것...

# 칼럼 아이디를 대문자로 바꿔야 Postman에서 동작됐는데 그러면 NotUniqueError가 일어나 다 소문자로 바꿔봄...