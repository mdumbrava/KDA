from flask import render_template, redirect, request, session
from . import bp
from KDA.dbase.db_kda import TblUsers
from KDA.user import getuser
from KDA import db
from werkzeug.security import check_password_hash, generate_password_hash


@bp.route('/')
def main():
    user=getuser()
    if user == "Guest":
        value = "Login and Registration Page"
        return render_template('Auth/Auth.html', value=value)
    else:
        return redirect ("/")

@bp.route('/login', methods=["POST"])
def login():
    print(request.form["user"])
    print(request.form["password"])
    data=TblUsers.query.filter_by(user=request.form["user"]).first()
    if data:
        print("user exists")
        if check_password_hash(data.password, request.form['password']):
            print("pass ok")
            session["USER_ID"] = request.form['user']
            return redirect ("/")
    else:
        print("user doesnt exist")
    return redirect ("/Auth")

@bp.route('/logout')
def logout():
    session.pop("USER_ID", None)
    return redirect ("/")

@bp.route('/register', methods=["POST"])
def register():
    print(request.form["user"])
    print(request.form["password"])
    check=TblUsers.query.filter_by(user=request.form["user"]).first()
    if request.form["password"] != request.form["password1"]:
        return "passwords do not match"
    if not check:
        data=TblUsers(user=request.form["user"], password=generate_password_hash(request.form["password"], "sha256"))
        db.session.add(data)
        db.session.commit()
        db.session.close()
        session["USER_ID"] = request.form['user']
        return redirect ("/")
    else:
        return "Username already exists"

@bp.route('/myaccount')
def myaccount():
    user=getuser()
    if user == 'Guest':
        return redirect ("/")
    value="My Account Settings"
    return render_template('Auth/myaccount.html', value=value)

@bp.route('/changepass', methods=["POST"])
def changepass():
    print(request.form["oldpassword"])
    print(request.form["newpassword"])
    print(request.form["newpassword1"])
    user=getuser()
    check=TblUsers.query.filter_by(user=user).first()
    if request.form["newpassword"] != request.form["newpassword1"]:
        return "new passwords do not match"
    check.password=password=generate_password_hash(request.form["newpassword"], "sha256")
    db.session.commit()
    db.session.close()
    return redirect ("/")
  