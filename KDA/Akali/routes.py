from flask import render_template
from . import bp
from KDA.user import getuser

@bp.route('/')
def main():
   user=getuser()
   value = "Welcome to Akali's Page"
   return render_template('Akali/Akali.html', value=value, user=user)