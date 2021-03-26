import requests


def get_imdb_json(titleid):
  url = "https://movie-database-imdb-alternative.p.rapidapi.com/"

  titleid = titleid

  querystring = {"i":titleid,"r":"json"}

  headers = {
      'x-rapidapi-key': "b53ac17182msh09e67e3bd75af88p1977f4jsnefbf58caf8cb",
      'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
      }

  response = requests.request("GET", url, headers=headers, params=querystring)

  return response.text

"""
{
  "Title": "Thelma & Louise",
  "Year": "1991",
  "Rated": "R",
  "Released": "24 May 1991",
  "Runtime": "130 min",
  "Genre": "Adventure, Crime, Drama",
  "Director": "Ridley Scott",
  "Writer": "Callie Khouri",
  "Actors": "Susan Sarandon, Geena Davis, Harvey Keitel, Michael Madsen",
  "Plot": "Two best friends set out on an adventure, but it soon turns around to a terrifying escape from being hunted by the police, as these two girls escape for the crimes they committed.",
  "Language": "English",
  "Country": "USA, UK, France",
  "Awards": "Won 1 Oscar. Another 23 wins & 50 nominations.",
  "Poster": "https://m.media-amazon.com/images/M/MV5BMjIxNDgzMDE2MF5BMl5BanBnXkFtZTcwNzY5NTk1NA@@._V1_SX300.jpg",
  "Ratings": [
    {
      "Source": "Internet Movie Database",
      "Value": "7.5/10"
    },
    {
      "Source": "Rotten Tomatoes",
      "Value": "84%"
    },
    {
      "Source": "Metacritic",
      "Value": "88/100"
    }
  ],
  "Metascore": "88",
  "imdbRating": "7.5",
  "imdbVotes": "137,893",
  "imdbID": "tt0103074",
  "Type": "movie",
  "DVD": "18 Jun 2016",
  "BoxOffice": "$45,360,915",
  "Production": "Metro Goldwyn Mayer",
  "Website": "N/A",
  "Response": "True"
}
"""