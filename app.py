from bs4 import BeautifulSoup
import requests
import feedparser
from flask import Flask, render_template, request, redirect
import os
from datetime import datetime
app = Flask(__name__)

year = datetime.now().year

@app.route('/', methods=['GET' , 'POST'])
def index():
    return render_template('index.html',year=year)
@app.route('/result', methods=['POST'])
def result():
    rss = request.form['rss']
    NewsFeed = feedparser.parse("https://vnexpress.net" + rss)
    return render_template('result.html',NewsFeed = NewsFeed,year=year)
@app.route('/detail', methods=['POST'])
def detail():
    link = request.form['link']
    soup = BeautifulSoup(requests.get(link).content,'html.parser')
    title = soup.find(class_="title_news_detail mb10").text
    paragraphs = soup.find("article")
    return """<h1>"""+title+"""</h1>""" + str(paragraphs) + '<a href="'+link+'">Link bài viết gốc</a>'
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    print("Starting app on port %d" % port)
app.run(debug=False, port=port, host='0.0.0.0')
