from Models.db import db
from datetime import datetime

class LoginCredentials(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(100))
     password= db.Column(db.String(100))
     timeLogged=db.Column(db.DateTime)

     def __init__(self,username,password):
          self.username=username
          self.password=password
          self.timeLogged=datetime.now()
