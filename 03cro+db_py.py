import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 타겟 URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20200303',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(data.text, 'html.parser')

# => 위는 크롤링을 하는 기본 코드
# 항상 기본 코드를 적고 시작해.

# 내가 받아 온 자료를 가지고 내가 분류하는 것 = 크롤링
# 요청 - > requests
# 분류 ->  bs4
# 크롤링은 사이트마다 다 생김새가 다르다.

trs = soup.select('#old_content > table > tbody > tr')

#old_content > table > tbody > tr:nth-child(2) >

for tr in trs:
   a_tag = tr.select_one('td.title > div > a')
   if a_tag is not None:
      rank = tr.select_one('td:nth-child(1) > img')['alt']
      star = tr.select_one('td.point').text
      title = a_tag.text
      doc = {
         'rank': rank,
         'title': title,
         'star': star
      }
      db.movies.insert_one(doc)