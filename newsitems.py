from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://punchng.com/frsc-foundations-partner-for-health-training-course/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('article', class_="single-article")

with open('punchnews4.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Authors', 'News']
    thewriter.writerow(header)

for list in lists:
        title = list.find('h1', class_="post-title").text.replace('\n', '')
        author = list.find('span', class_="post-author").text.replace('\n', '')
        news = list.find('div', class_="post-content").text.replace('\n', '')
        info = [title, author, news]
        print(info)
        thewriter.writerow(info)