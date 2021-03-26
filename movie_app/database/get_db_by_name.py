import requests

# url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

# movie_title = "Thunder Force"
# # year는 생략 가능
# querystring = {"s":movie_title,"page":"1","r":"json"} #"y":"2021"

# headers = {
#     'x-rapidapi-key': "b53ac17182msh09e67e3bd75af88p1977f4jsnefbf58caf8cb",
#     'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
#     }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
"""
{
  "Title": "Thunder Force",
  "Year": "2021",
  "imdbID": "tt10121392",
  "Type": "movie",
  "Poster": "https://m.media-amazon.com/images/M/MV5BMWZkM2I2NjEtNWM0Mi00MTgwLWJlYTAtYmNkZWYzNmQ1ZTBiXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_SX300.jpg"
}
이런 식으로 리턴함."""