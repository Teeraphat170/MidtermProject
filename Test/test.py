from flask import Flask,render_template,request
from urllib.parse import quote
from urllib.request import urlopen
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import urllib.parse
from models import db, Members
from ItemShop import ItemShop
from news import news
from ItemUpcoming import ItemUpcoming
from ItemAll import ItemAll
from about import about

app = Flask(__name__)
#app.register_blueprint(ItemShop)
#app.register_blueprint(news)
#app.register_blueprint(ItemUpcoming)
#app.register_blueprint(ItemAll)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///members.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(about)

db.init_app(app) 

@app.before_first_request
def create_table():
    db.create_all()

'''
headers = {
    'x-rapidapi-key': "68bb9b9c83msheb24ac34402b1e6p125c80jsn234cce83f901",
    'x-rapidapi-host': "fortnite4.p.rapidapi.com"
}
urlx = "https://fortnite4.p.rapidapi.com/items/all"
key = headers.get('x-rapidapi-key')

@app.route('/', methods=["GET","POST"])
def ItemAllx():
    word = request.args.get('word')
    xx = word
    r = ItemAlls(word, key ,xx)
    print(word)
    return render_template("test.html", r=r,xx=xx)

def ItemAlls(word, keys ,xx):
    urlx = "https://fortnite4.p.rapidapi.com/items/all"

    q = requests.request("GET", urlx, headers=headers).json()
    showitem = list()
    for x in range(2) :
        name = q['data'][x]['item']['name']
        rarity  = q['data'][x]['item']['rarity']
        type = q['data'][x]['item']['type']
        if name == word or rarity == word or type == word:
            showitem.append(q['data'][x]['item'])
        if not word:
            showitem.append(q['data'][x]['item'])
    return showitem
'''
app.run(debug=True,use_reloader=True)
