from flask import Flask,render_template,request,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
from flask_sqlalchemy import SQLAlchemy
import requests
import urllib.parse
from models import db, Members
from Blueprint.ItemShop import ItemShop
from Blueprint.news import news
from Blueprint.ItemUpcoming import ItemUpcoming
from Blueprint.ItemAll import ItemAll
from about import about

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///members.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app) 

@app.before_first_request
def create_table():
    db.create_all()

app.register_blueprint(ItemShop)
app.register_blueprint(news)
app.register_blueprint(ItemUpcoming)
app.register_blueprint(ItemAll)
app.register_blueprint(about)

app.run(debug=True,use_reloader=True)