from flask import Blueprint

bp = Blueprint('Kaisa', __name__, url_prefix='/Kaisa')

from . import routes