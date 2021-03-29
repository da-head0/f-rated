from flask import Blueprint, request, redirect, url_for, Response, render_template
from models.models import Movie
import pdb
from database.get_keywords import get_keyword, get_rottentomatoes
from database.get_db_by_tt import get_imdb_json
import json
from utils.recommendation import msg_processor

db = Blueprint('db', __name__)

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

# @movies.route('/db', methods=['POST'])
# def add_movie():
#     body = request.get_json()
#     #movie =  Movie(**body).save()
#     gettitle = body['Title']
#     getid = add_movie_by_json(body)
#     return f'{gettitle}이 추가되었습니다. \n ID = {getid}', 200

@db.route('/')
def index():
    return render_template('index.html')

@db.route('/db')
def movie_index():
    msg_code = request.args.get('msg_code', None)
    
    alert_msg = msg_processor(msg_code) if msg_code is not None else None

    movies = Movie.objects().order_by('-Year')

    return render_template('movie.html', alert_msg=alert_msg, movie_list=movies)

@db.route('/db/create/<imdbID>', methods=['POST']) #/<imdbID>
def add_movie_by_id(imdbID=None):
    searchmovie = Movie.objects(imdbID=imdbID).first()
    if searchmovie:
        return "영화가 이미 데이터베이스에 존재합니다", 403
    if not imdbID:
        return "IMDB id를 입력해주세요", 400
    else:
        newmovie_json = get_imdb_json(imdbID)
        json_obj = json.loads(newmovie_json)
        gettitle = json_obj['Title']
        getid = add_movie_by_json(json_obj)
        return f'{gettitle}이 추가되었습니다. \n ID = {getid}', 200
        #return redirect(url_for('db.movie_index', msg_code=1), code=400)

@db.route('/db/createbypage', methods=['GET','POST'])
def create_by_page():
    if request.method == 'POST':
        imdbid = request.form['imdbid']
        imdbid = str(imdbid)
        searchmovie = Movie.objects(imdbID=imdbid).first()

        if searchmovie:
            return "영화가 이미 데이터베이스에 존재합니다", 403
        if not imdbid:
            return "IMDB id를 입력해주세요", 400

        newmovie_json = get_imdb_json(imdbid)
        json_obj = json.loads(newmovie_json)
        add_movie_by_json(json_obj)
        msg = "영화가 성공적으로 추가되었습니다"
    return render_template('movie.html', msg=msg)
    #return redirect(url_for('db.movie_index', msg_code=0), code=400)

@db.route('/db/edit/<imdbID>', methods=['GET','PUT'])
def update_movie(imdbID):
    movie = Movie.objects(imdbID=imdbID).first()
    newkeywords = request.form['keywords']
    Movie(keywords = newkeywords).save() # 키워드 업데이트
    msg = f"영화가 성공적으로 수정되었습니다 \n 수정 내용 = {newkeywords}"
    return render_template('search.html', msg=msg)

@db.route('/db/delete/<imdbID>') #, methods=['DELETE']
def delete_movie(imdbID=None):
    movie = Movie.objects(imdbID=imdbID).first()
    if not imdbID:
      return "해당 Id를 가진 영화가 존재하지 않습니다", 400 # 상태코드만 줌
    if not movie:
      return "해당 영화가 존재하지 않습니다", 404
    delete_msg = f'IMDb ID가 {imdbID}인 영화를 삭제했습니다. \n 타이틀 : {movie.Title}'
    movie.delete()
    return render_template('movie.html', msg=delete_msg)
    #return f'IMDb ID가 {id}인 영화를 삭제했습니다. \n 타이틀 : {movie.Title}', 200
    #return redirect(url_for('db.movie_index', msg_code=3), code=200)


# def add_movie(genre=None):
# # 200 (OK)
# # 201 (Created)
# # 202 (Accepted)
# # 204 (No Content)
# # 301 (Moved Permanently)

#     #givemovie = request.get_json() # 데이터 있는거/없는거/user네임만 있는 거 3번 들어옴
#     #print("======================================givenuser : ", givenuser)
#     #username = givenuser["username"] # 유저네임 spongebob으로 잘 출력됨
#     # title = givemovie['Poster']
#     # return title
#     if request.method == 'GET':
#         ## 넘겨받은 숫자 
#         get_genre = request.args.get('genre')
#         ## 넘겨받은 문자
#         get_keyword = request.args.get('keyword')
#         ##넘겨받은 값을 원래 페이지로 리다이렉트
#     return render_template('input.html', genre=get_genre, keyword=get_keyword) #movie=givemovie



#     # if not username:
#     #   return "Needs username", 400
    
#     # try:
#     #   user = get_user(username) # json으로 id, name, 등 트위터 유저를 조회한 객체를 그대로 리턴, 잘 출력됨
#     # except Exception as e:
#     #   print(e)
#     #   return redirect(url_for('main.user_index', msg_code=1), code=400)

#     # # DB에 있는가?
#     # dbuser = User.query.filter_by(username=username).first()

#     # if dbuser: # db에 있으면
#     #   pass

#     # else: 
#     #   newuser = User(username=username, full_name = user.name, followers= user.followers_count)
#     #   db.session.add(newuser) # 유저 데이터베이스에 저장
#     #   db.session.commit()

#     #   # tweet 텍스트 + embedding 넣기
#     # txt = [[tw.full_text] for tw in get_tweets(username)]
#     # for tw in txt:
#     #   tw_emb = get_embeddings(tw)
#     #   tweet_up = Tweet(text=tw[0], embedding=tw_emb[0], user_id=newuser.id)
#     #   db.session.add(tweet_up)
#     #   db.session.commit()
#     #return redirect(url_for('main.user_index', msg_code=0), code=200)

# @bp.route('/user/')
# @bp.route('/user/<id>') # 이렇게 깔끔하게 뜨게 하라는 거지?
# def delete_movie(id=None):
#     """
#     delete_user 함수는 `user_id` 를 엔드포인트 값으로 넘겨주면 해당 아이디 값을 가진 유저를 데이터베이스에서 제거해야 합니다.

#     요구사항:
#       - HTTP Method: `GET`
#       - Endpoint: `api/user/<user_id>`

#     상황별 요구사항:
#       -  `user_id` 값이 주어지지 않은 경우:
#         - 리턴값: 없음
#         - HTTP 상태코드: `400`
#       - `user_id` 가 주어졌지만 해당되는 유저가 데이터베이스에 없는 경우:
#         - 리턴값: 없음
#         - HTTP 상태코드: `404`
#       - 주어진 `username` 값을 가진 유저를 정상적으로 데이터베이스에서 삭제한 경우:
#         - 리턴값: main_route.py 에 있는 user_index 함수로 리다이렉트 합니다.
#         - HTTP 상태코드: `200`
#     """

#     movie = Movie.objects(id=id).first()
#     print("===================user",movie)
#     if not id:
#       return "해당 Id를 가진 영화가 존재하지 않습니다", 400 # 상태코드만 줌
#     if not movie:
#       return "해당 영화가 존재하지 않습니다", 404

#     movie.delete()
#     return redirect(url_for('base', msg_code=3), code=200)
