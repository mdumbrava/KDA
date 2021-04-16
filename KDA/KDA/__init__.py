""" This package handles KDA Main Page app """
from flask import Blueprint

bp = Blueprint('KDA', __name__, url_prefix='/')

from . import routes