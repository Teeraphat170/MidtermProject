from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Members(db.Model):
    
    ID = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    surname = db.Column(db.String())
    sec_id = db.Column(db.Integer())
    picture = db.Column(db.String())



