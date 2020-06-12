from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# GEtting news from Times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html5lib')

toi_headings = toi_soup.find_all('h2')

toi_headings = toi_headings[0:-13] # removing footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)



#Getting news from Hindustan times

ht_r = requests.get("https://www.hindustantimes.com/india-news/")
ht_soup = BeautifulSoup(ht_r.content, 'html5lib')
ht_headings = ht_soup.findAll("div", {"class": "headingfour"})
ht_headings = ht_headings[2:]
ht_news = []

for hth in ht_headings:
    ht_news.append(hth.text)



#Getting news from Fox news
fox_r = requests.get("https://www.foxnews.com/politics")
fox_soup = BeautifulSoup(fox_r.content, "html5lib")

fox_headings = fox_soup.find_all('h4')
fox_headings = fox_headings[0:-13] #removing footers

fox_news = []

for fx in fox_headings:
    fox_news.append(fx.text)


#Getting news from Yahoo news
yh_r = requests.get("https://news.yahoo.com/politics/")
yh_soup = BeautifulSoup(yh_r.content, "html5lib")

yh_headings = yh_soup.find_all('h3')
yh_headings = yh_headings[0:-13] #removing footers

yh_news = []

for yh in yh_headings:
    yh_news.append(yh.text)



#Getting news from Huffpost news
hp_r = requests.get("https://www.huffpost.com/news/politics")
hp_soup = BeautifulSoup(hp_r.content, "html5lib")

hp_headings = hp_soup.find_all('h2')
hp_headings = hp_headings[0:-13] #removing footers

hp_news = []

for hp in hp_headings:
    hp_news.append(yh.text)





def index(req):
    return render(req, 'news/base.html', {'toi_news':toi_news, 'ht_news': ht_news, 'fox_news':fox_news,
     'yh_news':yh_news, 'hp_news':hp_news})