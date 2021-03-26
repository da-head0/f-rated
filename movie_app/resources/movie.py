from flask import Response, request
from database.models import Movie
from flask_restful import Resource

# flask-restful - uses a Class-based syntex
class MoviesApi(Resource):
    # 데이터를 전달 - 근데 지금 get으로 데이터 넘기면 업데이트 안됨 ㅋㅋ
    def get(self):
        query = Movie.objects()
        movies = Movie.objects().to_json()
        #Movie.objects(name="alice").first() 이거 하나 건드렸다가 ㅋㅋㅋㅋ 안됨.,...
        return Response(movies, mimetype="application/json", status=200)

    # 데이터의 값 변경 - post로 하면 업데이트 됨
    def post(self):
        body = request.get_json()
        movie =  Movie(**body).save() # 데이터 생성은 save로 한다
        id = movie.id
        return {'id': str(id)}, 200
        
class MovieApi(Resource):
    # Update
    def put(self, id):
        body = request.get_json()
        Movie.objects.get(id=id).update(**body)
        return '', 200
    
    def delete(self, id):
        movie = Movie.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        movies = Movie.objects.get(id=id).to_json()
        return Response(movies, mimetype="application/json", status=200)