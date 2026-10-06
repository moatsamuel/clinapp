from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from pkg.models import db, User 

users = Blueprint("users", __name__, template_folder='templates',static_folder='static')

@users.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # 1. Capture form data including phone
        fullname = request.form.get("fullname")
        email = request.form.get("email")
        phone = request.form.get("phone") # Capture phone number
        password = request.form.get("password")
        confirm_pass = request.form.get("confirm_pass")

        # 2. Check if passwords match
        if password != confirm_pass:
            return "Passwords do not match!"

        # 3. Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "Email is already registered. Please log in."

        # 4. Hash password
        password_hash = generate_password_hash(password)

        # 5. Create new User instance including phone
        new_user = User(
            fullname=fullname, 
            email=email, 
            phone=phone, # Save phone to database model
            password_hash=password_hash
        )

        # 6. Save to database
        db.session.add(new_user)
        db.session.commit()

        # 7. Redirect upon success
        return redirect(url_for('users.login'))

    return render_template("users/signup.html")


@users.route("/")
def index():
    return render_template("index.html")    


# @users.route("/login")
# def login():
#     return render_template("login.html")   

@users.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email != None and password != None:
            user = User.query.filter_by(email=email).first()
            if user and check_password_hash(user.password_hash, password):
                session['useronline'] = user.id # user is now logged in 
                return redirect(url_for('docs.home'))
            else:
                return redirect(url_for('users.login'))
        else:
            return redirect(url_for('users.login'))
    return render_template('users/login.html')



@users.route("/about")
def about():
    return render_template("about.html")       

# # @users.route("/signup")
# # def signup():
# #     return render_template("signup.html")
# @users.route('/signup', methods=['GET','POST'])
# def users_home():
#     if request.method == "POST":
#         fullname = request.form.get('fullname')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         password = request.form.get('password')
#         confirm_pass = request.form.get('confirm_password')
#         if fullname != None and email != None and phone != None and password != None and confirm_pass != None:
#             uname = User.query.filter_by(fullname=fullname).first()
#             email_addr = User.query.filter_by(email=email).first()
#             if uname or email_addr: #not uname or email_addr :
#                 return redirect(url_for('users.signup'))
#             else:
#                 if password == confirm_pass:
#                     password_hash = generate_password_hash(password)
#                     user = User(fullname=fullname, phone=phone, email=email, password_hash=password_hash)
#                     db.session.add(user)
#                     db.session.commit()
#                     return redirect(url_for('users.login'))
#                 else:
#                     return redirect(url_for('users.signup'))
#         else:
#             return redirect(url_for('users.index'))
#     return render_template('users/signup.html')



# # @users.route("/logins")
# # def log():
# #     return render_template("login.html")


@users.route("/contact", methods=("GET", "POST"))
def contact():
    if request.method == "POST":
        flash("Message received. expect to hear from us soonest", "success")
        redirect("/contact")
    return render_template("contact.html")

# @users.route("/contacts", methods=("GET", "POST"))
# def contact():
#     if request.method == "POST":
#         flash("Message received, Expect to hear from us soonest")
#         redirect("/")
#     return render_template("contact.html")


@users.route("/services")
def services():
    return render_template("services.html")

@users.route("/doctors")
def doc():
    return render_template("doctors.html")

@users.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@users.route("/usersoint1/")
def usersoint_1():
    return render_template("usersoint.html")

@users.route("/usersoint2/")
def usersoint_2():
    return render_template("usersoint2.html")

# @users.route("/dashboard/")
# def dashboard():
#     return render_template("dashboard.html")

