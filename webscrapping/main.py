from bs4 import BeautifulSoup
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
movies_web = response.text

soup = BeautifulSoup(movies_web,'html.parser')

titles = [title.getText() for title in soup.find_all(name='h3',class_='title')]

with open('./webscrapping/movies.txt','w',encoding='utf-8') as file:
    titles_ascending = titles[::-1]
    for title in titles_ascending:
        file.write(f'{title}\n')

