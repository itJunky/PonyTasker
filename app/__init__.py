from .settings import secret_key
from flask import Flask

tasker = Flask(__name__)
from app import views

tasker.secret_key = secret_key
