from flask import Blueprint, Response, request, render_template
from models.models import Movie
from database.get_keywords import get_keyword, get_rottentomatoes
from database.get_db_by_tt import get_imdb_json
from utils.recommendation import recommendation_by_title, msg_processor
import json

movies = Blueprint('movies', __name__)

# @movies.route('/movies') # 전체조회 - 이건 되는데...
# def get_movies():
#     movies = Movie.objects().to_json()
#     return Response(movies, mimetype="application/json", status=200)

# @movies.route('/searchbyid/<imdbid>', methods=['GET'])
# def search_movie_by_id(imdbid):
#     allmovie = Movie.objects(imdbID=imdbid).to_json() # json 파일 자체가 조회됨
#     return Response(allmovie, mimetype="application/json", status=200)

# @movies.route('/searchbytitle/<Title>', methods=['GET'])
# def search_movie_by_title(Title):
#     allmovie = Movie.objects(Title=Title) # 이렇게 하니까 models.py에 있는 repr이 실행되어 원하는 항목만 조회할 수 있음
#     return f'{allmovie}', 200

@movies.route('/gallery', methods=['GET'])
def gallery_poster():
    movies = Movie.objects(Poster__exists = True).order_by('-_id')[:100]
    #movies = Movie.objects(imdbRating__gte=5.0).order_by('-_id')[:100]
    return render_template('posters.html', movie_list=movies) #msg=delete_msg

@movies.route('/searchbykeyword', methods=['GET'])
def search_movie_by_keyword():
    keyword = request.args.get('keyword')
    keyword = str(keyword)
    searchbyid = Movie.objects.filter(keywords__icontains=keyword)
    #searchbyid = Movie.objects(tags__in=[keyword])
    #return Response(allmovie, mimetype="application/json", status=200)
    return render_template('search.html', movies = searchbyid) #msg=delete_msg

@movies.route('/searchbyid', methods=['GET'])
def search_movie_by_id():
    imdbid = request.args.get('imdbid')
    searchbyid = Movie.objects(imdbID=imdbid)
    #return Response(allmovie, mimetype="application/json", status=200)
    return render_template('search.html', movies = searchbyid) #msg=delete_msg

@movies.route('/searchbytitle', methods=['GET'])
def search_movie_by_title():
    title = request.args.get('movietitle')
    searchbytitle = Movie.objects(Title=title) # 이렇게 하니까 models.py에 있는 repr이 실행되어 원하는 항목만 조회할 수 있음
    #return f'{allmovie}', 200
    return render_template('search.html', movies=searchbytitle)

# @movies.route('/recommendation/<title>')
# def make_recommend_function(title):
#     movie = Movie.objects(Title=title).first()
#     # if not title:
#     #     return "영화 이름을 제대로 입력하세요. \n ex) Captain Marvel 같이 띄어쓰기 포함", 400
#     # if not movie:
#     #     return "입력하신 영화가 데이터베이스에 존재하지 않습니다. \n 여성 영화가 아닌가요?", 404
#     results = recommendation_by_title(title)
#     return Response(results, mimetype="application/json", status=200)
#     #return render_template('ml.html', movie_list = results) # msg=delete_msg

# 할수있어... 하자...
@movies.route('/recommendation', methods=['GET','POST'])
def test():
    if request.method == 'GET': #if request.method == 'POST':
        try:
            title = request.args.get('movie')
            movie = Movie.objects(Title=title).first()
            results = recommendation_by_title(title)
            if title:
                resultlist = []
                for mov in results:
                    mov_result = Movie.objects(Title=mov).first()
                    resultlist.append(mov_result)

                return render_template('ml2.html', movielist = results, movieinfo=movie, resultlist=resultlist)
            else:
                msg = "입력하신 영화가 데이터베이스에 존재하지 않습니다. \n 여성 영화가 아닌가요?"
                return render_template('ml2.html',msg=msg)

        except:
            return render_template('ml2.html')

    #return render_template('ml2.html') #, movielist = results, movieinfo=movie)


# @movies.route('/recomtest?movie=<title>')
# def please_recommend(title):
#     movietitle = str(title)
#     title = Movie.objects(Title=movietitle).first()
#     # if not title:
#     #     return "영화 이름을 제대로 입력하세요. \n ex) Captain Marvel 같이 띄어쓰기 포함", 400
#     # if not movie:
#     #     return "입력하신 영화가 데이터베이스에 존재하지 않습니다. \n 여성 영화가 아닌가요?", 404
#     results = recommendation_by_title(title)
#     #return Response(results, mimetype="application/json", status=200)
#     return render_template('ml2.html', results = results, movieinfo=title)

@movies.route('/recommendationbypage', methods=['GET','POST']) #recommendationbypage
def make_recommend_function_by_page():
    if request.method == 'POST':
        movietitle = request.form['movie']
        movietitle = str(movietitle)
        title = Movie.objects(Title=movietitle).first()
    # if not title:
    #     return "영화 이름을 제대로 입력하세요. \n ex) Captain Marvel 같이 띄어쓰기 포함", 400
    # if not movie:
    #     return "입력하신 영화가 데이터베이스에 존재하지 않습니다. \n 여성 영화가 아닌가요?", 404
        results = recommendation_by_title(title)
    #return Response(results, mimetype="application/json", status=200)
        return render_template('ml2.html', results = results, movieinfo=title) # msg=delete_msg


#@movies.route('/searchbytitle/<title>')
# def searchmovie(input):
#     for mov in Movie.objects(title__contains=input):
#      print ('Title:', mov.title)