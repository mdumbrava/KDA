from flask import render_template
from . import bp
from KDA.user import getuser

@bp.route('/')
def main():
   user=getuser()
   value = "Welcome to Evelynn's Page"
   return render_template('Evelyn/Evelyn.html', value=value, user=user)