import requests

"""

ex) naver news ranking
for some site you need to give your header
---
import requests
url = "your url"
response = requests.get(url)
---
---
import requests
url = "your url"
header = {"User-Agent":"your_agent"}
response = requests.get(url,headers=header)

"""

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
url = "https://news.naver.com/main/ranking/popularDay.naver"
response = requests.get(url, headers=headers)

import bs4

soup = bs4.BeautifulSoup(response.text, features='html.parser')

ranking_news = soup.find('div', class_="_officeCard _officeCard0").find_all('div', class_='rankingnews_box')

for news in ranking_news:
    news_name = news.find('strong', class_='rankingnews_name').get_text(strip=True)
    print(news_name)
    for i, titles in enumerate(news.find_all('a', class_="list_title nclicks('RBP.rnknws')")):
        print(f"{i + 1} : ", titles.get_text(strip=True))
