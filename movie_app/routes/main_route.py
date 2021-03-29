from flask import Blueprint, render_template, request
#from twit_app.utils import main_funcs
from database import db
from models.models import Movie #, Ratings
import pdb

bp = Blueprint('main', __name__)

@bp.route('/detail')
def moviedetail():
    return render_template('detail/moviedetail.html')

@bp.route('/movielist', methods=["GET", "POST"])
def movie_list():
    """
    users 에 유저들을 담아 넘겨주세요. 각 유저 항목은 다음과 같은 딕셔너리
    형태로 넘겨주셔야 합니다.
     -  {
            "id" : "유저의 아이디 값이 담긴 숫자",
            "username" : "유저의 유저이름 (username) 이 담긴 문자열"
        }

    prediction 은 다음과 같은 딕셔너리 형태로 넘겨주셔야 합니다:
     -   {
             "result" : "예측 결과를 담은 문자열입니다",
             "compare_text" : "사용자가 넘겨준 비교 문장을 담은 문자열입니다"
         }
    """
    movies = Movie.query.all()
    #prediction = None

    # if request.method == "POST":
    #     user_1_given = request.form["user_1"]
    #     user_2_given = request.form["user_2"]
    #     input_text = request.form["compare_text"]
    #     # 왜 id == username 인데 동작할까...
    #     user1 = User.query.filter(User.id==user_1_given).first()
    #     user2 = User.query.filter(User.id==user_2_given).first()
    #     user_list = [user1, user2]
    #     prediction["result"] = main_funcs.predict_text(user_list, input_text)
    #     prediction["compare_text"] = input_text

         
    return render_template('base/base.html', movies=movies), 200

# @bp.route('/user')
# def user_index():
#     """
#     user_list 에 유저들을 담아 템플렛 파일에 넘겨주세요
#     """
#     msg_code = request.args.get('msg_code', None)
    
#     alert_msg = main_funcs.msg_processor(msg_code) if msg_code is not None else None

#     users = User.query.all()

#     return render_template('user.html', alert_msg=alert_msg, user_list=users)
