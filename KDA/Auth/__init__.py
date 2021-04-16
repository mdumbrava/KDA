""" This package handles Auth app """
from flask import Blueprint

bp = Blueprint('Auth', __name__, url_prefix='/Auth')

from . import routes