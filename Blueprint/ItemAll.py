from flask import Flask,render_template,request,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import urllib.parse

ItemAll = Blueprint('ItemAll', __name__)

headers = {
    'x-rapidapi-key': "f5190a5977mshf4f4bd75f0232f4p1bd172jsn05e6db837ac3",
    'x-rapidapi-host': "fortnite4.p.rapidapi.com"
    }
#key = headers.get('x-rapidapi-key')

@ItemAll.route('/ItemSeach', methods=["GET","POST"])
def ItemAllx():
    word = request.args.get('word')
    r = ItemAlls(word)
    return render_template("ItemAll.html", r=r,word=word)

def ItemAlls(word):
    urlx = "https://fortnite4.p.rapidapi.com/items/all"

    q = requests.request("GET", urlx, headers=headers).json()
    showitem = list()

    for x in range(20) :
    #for x in range(len(q['data'])) :
        name = q['data'][x]['item']['name']
        rarity  = q['data'][x]['item']['rarity']
        type = q['data'][x]['item']['type']
        
        if name == word or rarity == word or type == word:
            showitem.append(q['data'][x]['item'])
        if not word:
            showitem.append(q['data'][x]['item'])
    return showitem