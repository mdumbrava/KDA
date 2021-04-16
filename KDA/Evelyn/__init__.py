from flask import Blueprint

bp = Blueprint('Evelyn', __name__, url_prefix='/Evelyn')

from . import routes