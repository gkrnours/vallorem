from vallorem.model.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_mail = db.Column(db.Integer, db.ForeignKey('mail.id'))
    password = db.Column(db.String(50))

    def __init__(self, id_mail, password):
        self.id_mail = id_mail
        self.password = password
