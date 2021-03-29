import csv
import os
from pymongo import MongoClient
import get_db_by_tt
import json
import pandas as pd
import requests
from get_keywords import get_keyword, get_rottentomatoes
from movie_app.models.models import Movie

host = 'cluster0.xc44g.mongodb.net'
user = 'aimb'
password = 'mimomimo'
database_name = 'frated'
collection_name = 'test'

client = MongoClient(f"mongodb+srv://{user}:{password}@{host}/{database_name}?retryWrites=true&w=majority")

db = client.frated

df = pd.read_csv('f2movies.csv')

# f-rated 지수가 2.0 이상인 영화들의 title id 추출
# f_df = df[df['f-rated'] >= 2.0]
# f_df = f_df.reset_index(drop=True)
#flist = df['imdb_title_id'].tolist()

def add_movie_by_json(body):
    newmovie = Movie(
        imdbID = body['imdbID'],
        Title = body['Title'], 
        Year = body['Year'],
        Rated = body['Rated'],
        Released = body['Released'], # datetime으로 바꿀 수 있을듯
        Runtime = body['Runtime'], 
        Genre = body['Genre'],
        Director = body['Director'],
        Writer = body['Writer'],
        Actors = body['Actors'],
        Plot = body['Plot'],
        Language = body['Language'],
        Country = body['Country'],
        Awards = body['Awards'],
        Poster = body['Poster'],
        Ratings = body['Ratings'], 
        Metascore = body['Metascore'],
        imdbRating = body['imdbRating'],
        imdbVotes = body['imdbVotes'],
        BoxOffice = body['BoxOffice'],
        Production = body['Production'],
        keywords = get_keyword(body['imdbID']),
        RottenTomatoes = get_rottentomatoes(body),
        Genre1 = body['Genre'].split(',')[0]).save()
    return newmovie.id
    
flist = ['tt2294629', 'tt0103074']
# # 몽고db에 데이터 넣기
for title in flist:
    jsondata = get_db_by_tt.get_imdb_json(title) # 작동 잘 됨
    value = json.loads(jsondata)
    add_movie_by_json(value)
    # newmovie = Movie(
    #     keywords = get_keyword(body['imdbID']),
    #     RottenTomatoes = get_rottentomatoes(body),
    #     Genre1 = body['Genre'].split(',')[0]).save()
# 일단 작동 잘 됨
# 888개 영화 추가 완료

