import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.genie

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713', headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')


songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for song in songs:
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    singer = song.select_one('td.info > a.artist.ellipsis').text
    rank = song.select_one('td.number').text[0:2].strip()

    doc = {
        'rank': rank,
        'title': title,
        'singer': singer
        }

    db.songs.insert_one(doc)

# 디비명이랑 컬렉션 명이랑 똑같네요! 보통은 다르게 하는 게 더 좋습니다! 디비명을 genie, 컬렉션 명을 songs면 좋을 것 같네요! 수고하셨습니다~~