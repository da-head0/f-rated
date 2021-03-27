from flask import Blueprint, request, redirect, url_for, Response, render_template
# from twit_app.services import tweepy_api, embedding_api
# from twit_app.models import user_model, tweet_model
from models.models import Movie, Ratings
# from twit_app.models.tweet_model import Tweet
# from twit_app import db
# from twit_app.services.tweepy_api import get_user, get_tweets
# from twit_app.services.embedding_api import get_embeddings
import pdb

bp = Blueprint('input', __name__)


@bp.route('/input', methods=['GET', 'POST'])
def get_genre(genre=None):
# 200 (OK)
# 201 (Created)
# 202 (Accepted)
# 204 (No Content)
# 301 (Moved Permanently)

    #givemovie = request.get_json() # 데이터 있는거/없는거/user네임만 있는 거 3번 들어옴
    #print("======================================givenuser : ", givenuser)
    #username = givenuser["username"] # 유저네임 spongebob으로 잘 출력됨
    # title = givemovie['Poster']
    # return title
    if request.method == 'GET':
        ## 넘겨받은 숫자 
        get_genre = request.args.get('genre')
        ## 넘겨받은 문자
        get_keyword = request.args.get('keyword')
        ##넘겨받은 값을 원래 페이지로 리다이렉트
    return render_template('input.html', genre=get_genre, keyword=get_keyword) #movie=givemovie



    # if not username:
    #   return "Needs username", 400
    
    # try:
    #   user = get_user(username) # json으로 id, name, 등 트위터 유저를 조회한 객체를 그대로 리턴, 잘 출력됨
    # except Exception as e:
    #   print(e)
    #   return redirect(url_for('main.user_index', msg_code=1), code=400)

    # # DB에 있는가?
    # dbuser = User.query.filter_by(username=username).first()

    # if dbuser: # db에 있으면
    #   pass

    # else: 
    #   newuser = User(username=username, full_name = user.name, followers= user.followers_count)
    #   db.session.add(newuser) # 유저 데이터베이스에 저장
    #   db.session.commit()

    #   # tweet 텍스트 + embedding 넣기
    # txt = [[tw.full_text] for tw in get_tweets(username)]
    # for tw in txt:
    #   tw_emb = get_embeddings(tw)
    #   tweet_up = Tweet(text=tw[0], embedding=tw_emb[0], user_id=newuser.id)
    #   db.session.add(tweet_up)
    #   db.session.commit()
    #return redirect(url_for('main.user_index', msg_code=0), code=200)

@bp.route('/user/')
@bp.route('/user/<int:user_id>') # 이렇게 깔끔하게 뜨게 하라는 거지?
def delete_user(user_id=None):
    """
    delete_user 함수는 `user_id` 를 엔드포인트 값으로 넘겨주면 해당 아이디 값을 가진 유저를 데이터베이스에서 제거해야 합니다.

    요구사항:
      - HTTP Method: `GET`
      - Endpoint: `api/user/<user_id>`

    상황별 요구사항:
      -  `user_id` 값이 주어지지 않은 경우:
        - 리턴값: 없음
        - HTTP 상태코드: `400`
      - `user_id` 가 주어졌지만 해당되는 유저가 데이터베이스에 없는 경우:
        - 리턴값: 없음
        - HTTP 상태코드: `404`
      - 주어진 `username` 값을 가진 유저를 정상적으로 데이터베이스에서 삭제한 경우:
        - 리턴값: main_route.py 에 있는 user_index 함수로 리다이렉트 합니다.
        - HTTP 상태코드: `200`
    """

    user = User.query.filter_by(id=user_id).one_or_none()
    print("===================user",user)
    if not user_id:
      return Response(status=400) # 상태코드만 줌
    if not user:
      return Response(status=404)

    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('main.user_index', msg_code=3), code=200)
