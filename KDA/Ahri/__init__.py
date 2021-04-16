from flask import Blueprint

bp = Blueprint('Ahri', __name__, url_prefix='/Ahri')

from . import routes