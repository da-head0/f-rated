import csv
import os
from pymongo import MongoClient
import get_db_by_tt
import json
import pandas as pd

host = 'cluster0.xc44g.mongodb.net'
user = 'aimb'
password = 'mimomimo'
database_name = 'frated'
collection_name = 'test'


client = MongoClient(f"mongodb+srv://{user}:{password}@{host}/{database_name}?retryWrites=true&w=majority")

db = client.frated

# with open('imdb_0326.json') as json_file:
#     json_data = json.load(json_file)
# for title in json_data:
#     db.movie.insert_one(title)

# ServerStat = db.command("serverStatus")
# print(ServerStat)

# df = pd.read_csv('f2movies.csv')

# # f-rated 지수가 2.0 이상인 영화들의 title id 추출
# f_df = df[df['f-rated'] >= 2.0]
# f_df = f_df.reset_index(drop=True)
# flist = f_df['imdb_title_id'].tolist()

# # 몽고db에 데이터 넣기
# for title in flist:
#     jsondata = get_db_by_tt.get_imdb_json(title) # 작동 잘 됨
#     value = json.loads(jsondata)
#     db.imdb.insert_one(value)

# 888개 영화 추가 완료

