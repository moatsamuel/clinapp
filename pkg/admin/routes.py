
from flask import Blueprint, render_template, request, redirect, flash, url_for
from pkg.models import db, Specialty, Doctor

admin = Blueprint('admin',__name__,template_folder='templates',static_folder='static')


@admin.route("/specialty")
def special():
    specialty = Specialty(name='Dermatology', description='They are trained to diagnose and treat variety of skin, hair, and nail conditions', status='available')
    # specialty2 = Specialty(name='Cardiology', description='They are expert in heart  and blood vessel diseases', status='available')
    # specialty3 = Specialty(name='Paediatrics', description='They are specialze in treating children', status='Not available')
    # specialty4 = Specialty(name='Orthopedic', description='They are expert in health and function of musculoskeletal system', status='available')
    db.session.add(specialty)
    db.session.commit()
    return 'Specialty Created Successfully'

@admin.route("/create_doctors/")
def doctors():
    # doctor1 = Doctor(first_name='Mark', last_name='Brenda', email='mark_smith123@gmail.com', phone='2348087321885', specialty_id='2', availability= 'Not Available', licence_number='LC1059009')
    # doctor2 = Doctor(first_name='Dami', last_name='Dangote', email='Dami.dangote@gmail.com', phone='2348087324459', specialty_id='1', availability= 'Available', licence_number='LC1059889')
    # doctor3 = Doctor(first_name='James', last_name='Bezos', email='jamesbezos@gmail.com', phone='23480873208957', specialty_id='4', availability= 'Available', licence_number='LC1059098')
    # doctor4 = Doctor(first_name='Adewale', last_name='Musk', email='ade_musk@gmail.com', phone='2348087321134', specialty_id='3', availability= 'Available', licence_number='LC1059123')
    # doctor5 = Doctor(first_name='Ernest', last_name='Roi', email='roi@yahoo.com', phone='2348087323456', specialty_id='2', availability= 'Not Available', licence_number='LC1059321')
    # doctor6 = Doctor(first_name='Peace', last_name='Peace', email='peace@yahoo.com', phone='2348087324344', specialty_id='4', availability= 'Not Available', licence_number='LC1059451')
    # doctor7 = Doctor(first_name='Naomi', last_name='Joseph', email='naomi.j@gmail.com', phone='2348087320087', specialty_id='3', availability= 'Available', licence_number='LC1059765')
    doctor = Doctor(first_name='Jorja', last_name='Smith', email='jorja@gmail.com', phone='2348087320087', specialty_id='3', availability= 'Available', licence_number='LC1059700')
    # db.session.add_all([doctor1, doctor2, doctor3, doctor4, doctor5, doctor6, doctor7])
    db.session.add(doctor)
    db.session.commit()
    return 'Doctors Created Successfully'
