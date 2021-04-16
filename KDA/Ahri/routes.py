from flask import render_template
from . import bp
from KDA.user import getuser

@bp.route('/')
def main():
   user=getuser()
   value = "Welcome to Ahri's Page"
   return render_template('Ahri/Ahri.html', value=value, user=user)


