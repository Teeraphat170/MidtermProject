from flask import Flask,render_template,request,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import urllib.parse

news = Blueprint('new', __name__)

headers = {
    'x-rapidapi-key': "f5190a5977mshf4f4bd75f0232f4p1bd172jsn05e6db837ac3",
    'x-rapidapi-host': "fortnite4.p.rapidapi.com"
    }

@news.route('/')
def new():
    x = newsx()
    return render_template('news.html',x=x)

def newsx():
    url = "https://fortnite4.p.rapidapi.com/news"

    url = requests.request("GET", url, headers=headers)
    q = url.json()
    show = []
    for z in range(len(q['data'])) :
        img =  q['data'][z]['image']
        title =  q['data'][z]['title']
        body =  q['data'][z]['body']
        platform =   q['data'][z]['platform']
        show.append({"img":img,"title":title,"body":body,"platform":platform})
    return show