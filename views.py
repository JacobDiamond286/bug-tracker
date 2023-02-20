from flask import Blueprint, render_template

views = Blueprint(__name__, 'views')

@views.route("/")
def base():
    return render_template("base.html")
    
@views.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@views.route("/login")
def login():
    return render_template("login.html")

@views.route("/register")
def register():
    return render_template("register.html")

@views.route("/forgot-password")
def forgot():
    return render_template("forgotpassword.html")