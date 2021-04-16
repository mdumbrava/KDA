from flask import render_template, redirect, request, session
from . import bp
from KDA.dbase.db_kda import TblComments
from KDA import db
from KDA.user import getuser
from datetime import date

@bp.route('/')
@bp.route('/<page>')
def KDA(page=None):
   if page:
      page=int(page)
   else:
      page=1
   user=getuser()
   value = "WELCOME TO HOMEPAGE OF KDA"
   data=TblComments.query.order_by(TblComments.id.desc()).paginate(per_page = 6, page = page)
   db.session.close()
   size=len(data.items)
   return render_template('KDA.html', value=value, data=data, size=size, user=user) 

@bp.route('/add', methods=['POST'])
def add():
   data=TblComments(user=session["USER_ID"], comments=request.form['comments'], time=date.today())
   db.session.add(data)
   db.session.commit()
   db.session.close()
   return redirect("/")

@bp.route('/form/<id>')
def form(id):
   print (id)
   data=TblComments.query.filter_by(id=id).first()
   return render_template('form.html' , data=data) 

@bp.route('/update', methods=['POST'])
def update():
   data=TblComments.query.filter_by(id=request.form["id"]).first()
   data.user=request.form["user"]
   data.comments=request.form["comments"]
   db.session.commit()
   db.session.close()
   return redirect("/")

@bp.route('/delete/<id>')
def delete(id):
   data=TblComments.query.filter_by(id=id).first()
   db.session.delete(data)
   db.session.commit()
   db.session.close()
   return redirect("/")

# @bp.route('/sel_page/<page>')
# def sel_page(page):
#    user=getuser()
#    value = "WELCOME TO HOMEPAGE OF KDA"
#    data=TblComments.query.order_by(TblComments.id.desc()).paginate(per_page = 6, page = int(page))
#    db.session.close()
#    size=len(data.items)
#    return render_template('KDA.html', value=value, data=data, size=size, user=user) 