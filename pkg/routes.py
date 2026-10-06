
# from flask import Blueprint, render_template, request, redirect, flash, url_for


# users = Blueprint('users',__name__,template_folder='templates',static_folder='static')


# @users.route("/")
# def index():
#     return render_template("index.html")       


# # @users.route("/about")
# # def about():
# #     return render_template("about.html")       

# @users.route("/signup")
# def signup():
#     return render_template("signup.html")

# # @users.route("/login")
# # def login():
# #     return render_template("login.html")

# @users.route("/logins")
# def log():
#     return render_template("login.html")


# # @users.route("/contact", methods=("GET", "POST"))
# # def contact():
# #     if request.method == "POST":
# #         flash("Message received. expect to hear from us soonest", "success")
# #         redirect("/contact")
# #     return render_template("contact.html")

# @users.route("/contacts", methods=("GET", "POST"))
# def contact():
#     if request.method == "POST":
#         flash("Message received, Expect to hear from us soonest")
#         redirect("/")
#     return render_template("contact.html")


# @users.route("/services")
# def services():
#     return render_template("services.html")

# @users.route("/doctors")
# def doc():
#     return render_template("doctors.html")

# @users.errorhandler(404)
# def not_found(e):
#     return render_template("404.html")

# @users.route("/usersoint1/")
# def usersoint_1():
#     return render_template("usersoint.html")

# @users.route("/usersoint2/")
# def usersoint_2():
#     return render_template("usersoint2.html")

# @users.route("/dashboard/")
# def dashboard():
#     return render_template("dashboard.html")