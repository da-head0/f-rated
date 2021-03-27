from models.models import Movie

def searchkeyword(keyword):
    # object 뒤에는 class__
    return Movie.objects(title__contains=keyword)
            #movies = Movie.objects(title="Daisies") #이거 하나 건드렸다가 ㅋㅋㅋㅋ 안됨.,...
        #print(movies)
        #return movies, 200


def imdbratingover(num):
    return Movie.objects(imdbRating__gte=num)


searchkeyword('Captain Marvel')