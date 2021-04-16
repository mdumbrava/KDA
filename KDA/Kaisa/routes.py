from flask import render_template
from . import bp
from KDA.user import getuser

@bp.route('/')
def main():
   user=getuser()
   value = "Welcomes to Kai'sa Page"
   return render_template('Kaisa/Kaisa.html', value=value, user=user)