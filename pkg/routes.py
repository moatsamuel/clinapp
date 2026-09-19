
from flask import render_template, request, redirect, flash
from pkg import app


@app.route("/")
def index():
    return render_template("index.html")       


# @app.route("/about")
# def about():
#     return render_template("about.html")       

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/contact", methods=("GET", "POST"))
def contact():
    if request.method == "POST":
        flash("Message received. expect to hear from us soonest", "success")
        redirect("/contact")
    return render_template("contact.html")



@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/doctors")
def doc():
    return render_template("doctors.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")