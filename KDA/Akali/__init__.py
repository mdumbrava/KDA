from flask import Blueprint

bp = Blueprint('Akali', __name__, url_prefix='/Akali')

from . import routes