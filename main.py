import requests
import re
from bs4 import BeautifulSoup



url ="https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)


soup = BeautifulSoup(response.content,'html.parser')

title_tags = soup.find_all("h3",class_='title')

titles = []

for title_tag in title_tags:
    titles.append(title_tag.getText())



titles.reverse()


with open("top_100_movies.txt",'wb') as f:
    for i,title in enumerate(titles):
        if not title[0].isdigit():
            f.write(f"{i + 1}) {title}\n".encode('utf-8'))
        else:
            f.write((title + '\n').encode('utf-8'))













