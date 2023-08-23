from flask import Flask

tasker = Flask(__name__)
from app import views
