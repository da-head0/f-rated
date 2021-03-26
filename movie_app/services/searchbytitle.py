from movie_app.database.models import Movie

def searchkeyword(keyword):
    # object 뒤에는 class__
    return Movie.objects(title__contains=keyword)


def imdbratingover(num):
    return Movie.objects(imdbRating__gte=num)