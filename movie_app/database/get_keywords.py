import pandas as pd

# df 연동해야함
#movies_index = df.imdbID
# 전체 db가 아닌 요청한 id만 얻어오게 하기

from tqdm import tqdm
from time import sleep
from imdb import IMDb
ia = IMDb()

def get_keyword(imdbID):
    keyworddic = ia.get_movie_keywords(imdbID[2:])
    keys = keyworddic['data']['keywords'][:5]
    return keys

def get_rottentomatoes(movie):
    rt = movie['Ratings'][1]['Value']
    if rt.endswith('%'):
      return rt
    else:
      st = movie['Ratings'][0]['Value']
      if st.endswith('%'):
        return st
      else:
        return 'N/A'