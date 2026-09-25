import os
from dotenv import load_dotenv
from flask import Flask
app = Flask(__name__)

from pkg import routes

app.secret_key = os.getenv("SECRET_KEY")

load_dotenv()