from flask import Flask,render_template,request,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import urllib.parse
import os

ItemShop = Blueprint('ItemShop', __name__)

headers = {
        'x-rapidapi-key': "f5190a5977mshf4f4bd75f0232f4p1bd172jsn05e6db837ac3",
        'x-rapidapi-host': "fortnite4.p.rapidapi.com"
    }
@ItemShop.route("/ItemShop")
def home():
    r= Item()
    return render_template("home.html",r=r)

def Item(): #ItemShop
    url = "https://fortnite4.p.rapidapi.com/shop/"

    url = requests.request("GET", url, headers=headers)
    r = url.json()
    show = []
    for x in range(len(r['data'])) :
        name =  r['data'][x]['item']['name']
        rarity =  r['data'][x]['item']['rarity']
        types =  r['data'][x]['item']['type']
        img =   r['data'][x]['item']['images']['icon']
        cost = r['data'][x]['store']['cost']
        show.append({"name":name,"rarity":rarity,"types":types,"img":img,"cost":cost})
    return show