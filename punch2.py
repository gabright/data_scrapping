from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://punchng.com/topics/interview/page/7/"
page = requests.get(url)
links = []
soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('h1', class_="post-title")

with open('punchinterview7.csv', 'w', encoding='utf8', newline='') as f:
      thewriter = writer(f)
      header = ['Title', 'Dates', 'Authors', 'News']
      thewriter.writerow(header)
      for list in lists:
        titles = list.find('a')
        url = titles["href"]

        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'html.parser')
        lists = soup.find_all('article', class_="single-article")

        for list in lists:
                  title = list.find('h1', class_="post-title").text.replace('\n', '')
                  dates = list.find('span', class_="post-date").text.replace('\n', '')
                  authors = list.find('span', class_="post-author").text.replace('\n', '')
                  news = list.find('div', class_="post-content").text.replace('\n', '')
                  info = [title, dates, authors, news]
                  print(info)

                  thewriter.writerow(info)