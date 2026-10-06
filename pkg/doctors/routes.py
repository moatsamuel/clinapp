# from flask import Blueprint, render_template, request, redirect, flash, url_for


# doctors = Blueprint('doctors',__name__,template_folder='templates',static_folder='static')


# @doctors.route("/doctor-details", methods=["GET", "POST"]) 
# def doctor_details():
#     if request.method == "POST":

#         license_number = request.form.get("license_number")
#         specialty = request.form.get("specialty")
#         phone = request.form.get("phone")
#         experience = request.form.get("experience")

#         # Later we will save everything to the database

#         return "Doctor account created successfully"

#     return render_template("doctor_details.html")
