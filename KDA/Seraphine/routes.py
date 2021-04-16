from flask import render_template
from . import bp
from KDA.user import getuser

@bp.route('/')
def main():
   user=getuser()
   value = "Welcome to Seraphine's Page"
   return render_template('Seraphine/Seraphine.html', value=value, user=user)