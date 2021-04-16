from KDA import db

class TblComments(db.Model):
    __tablename__ = 'tblcomments'

    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50))
    time = db.Column(db.String(50))
    comments = db.Column(db.String(1000))