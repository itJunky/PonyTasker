from .settings import secret_key
from flask import Flask
from pony.flask import Pony

tasker = Flask(__name__)
from app import views
Pony(tasker)

tasker.secret_key = secret_key
