import requests
from bs4 import BeautifulSoup

titleid = 'tt0103074'
testurl = f"https://www.imdb.com/title/{titleid}/reviews?ref_=tt_ql_3" # Most Helpful

r = requests.get(url=testurl)
# create a BeautifulSoup object
soup = BeautifulSoup(r.text, 'html.parser')

# Top 5 review
con = soup.find_all("div",{'class':'text show-more__control'})[:4]
for c in con:
    print(c.text)

# # Genre list

# ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'Film Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Short', 'Sport', 'Superhero', 'Thriller', 'War', 'Western']

# r = requests.get(url='https://www.imdb.com/feature/genre/?ref_=nv_ch_gr')
# soup = BeautifulSoup(r.text, 'html.parser')

# # Top 5 review
# con = soup.find_all("div",{'class':'table-cell'})
# genrelist = []
# for c in con:
#     genrelist.append(c.text.strip())

# print(genrelist)