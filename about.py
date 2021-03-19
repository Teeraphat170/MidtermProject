from flask import Flask,render_template,request,Blueprint
from urllib.parse import quote
from urllib.request import urlopen
from flask_sqlalchemy import SQLAlchemy
import json
import requests
import urllib.parse
from models import db, Members

about = Blueprint('about',__name__)

@about.route('/about')
def aboutx():
   return render_template('datalist.html', members = Members.query.all() )