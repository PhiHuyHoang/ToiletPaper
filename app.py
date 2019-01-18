from bs4 import BeautifulSoup
import requests
import feedparser
from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/', methods=['GET' , 'POST'])
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def result():
    rss = request.form['rss']
    NewsFeed = feedparser.parse("https://vnexpress.net" + rss)
    for entry in NewsFeed.entries:
        print(entry.title, entry.link)
    return render_template('result.html',NewsFeed = NewsFeed)
@app.route('/detail', methods=['POST'])
def detail():
    link = request.form['link']
    soup = BeautifulSoup(requests.get(link).content,'html.parser')
    paragraphs = soup.find(class_="content_detail fck_detail width_common block_ads_connect")
    return str(paragraphs)
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    print("Starting app on port %d" % port)
app.run(debug=False, port=port, host='0.0.0.0')
