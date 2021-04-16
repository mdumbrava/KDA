from flask import Blueprint

bp = Blueprint('Seraphine', __name__, url_prefix='/Seraphine')

from . import routes