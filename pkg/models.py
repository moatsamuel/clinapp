from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Specialty(db.Model):
    __tablename__ = 'specialties'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.Text)
    status = db.Column(db.Enum('Not available','Available', default='Not available'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    doctors = db.relationship("Doctor",backref='specialty')




class Doctor(db.Model):
    __tablename__ = 'doctors'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    phone = db.Column(db.Integer, nullable=False)
    specialty_id = db.Column(db.Integer, db.ForeignKey('specialties.id'))
    availability = db.Column(db.Enum('Not available','Available', default='Not available'), nullable=False)
    licence_number = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

