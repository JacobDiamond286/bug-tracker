from flask import Blueprint, render_template

views = Blueprint(__name__, 'views')

@views.route("/")
def base():
    return render_template("base.html")
    
@views.route("/home")
def home():
    return render_template("home.html")

@views.route("/login")
def login():
    return render_template("login.html")

@views.route("/test")
def test():
    return render_template("register.html")