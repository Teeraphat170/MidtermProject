from flask import Flask,render_template,request,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import urllib.parse

ItemUpcoming = Blueprint('ItemUpcoming', __name__)

headers = {
    'x-rapidapi-key': "f5190a5977mshf4f4bd75f0232f4p1bd172jsn05e6db837ac3",
    'x-rapidapi-host': "fortnite4.p.rapidapi.com"
    }
@ItemUpcoming.route('/Item (Upcoming)')
def ItemUpcomingx():
    r= ItemUpcomings()
    return render_template("ItemUpcoming.html", r=r)

def ItemUpcomings():
    url = "https://fortnite4.p.rapidapi.com/items/upcoming"

    url = requests.request("GET", url, headers=headers)
    w = url.json()
    show = []
    for x in range(len(w['data'])) :
        name =  w['data'][x]['item']['name']
        description = w['data'][x]['item']['description']
        rarity = w['data'][x]['item']['rarityName']
        types = w['data'][x]['item']['type']
        source = w['data'][x]['item']['images']['icon']
        setName = w['data'][x]['item']['setName']
        show.append({"name":name,"description":description,"rarity":rarity,"types":types,"source":source,"setName":setName})
    return show