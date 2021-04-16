from KDA import db

class TblUsers(db.Model):
    __tablename__ = 'tblusers'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50))
    password = db.Column(db.String(100))