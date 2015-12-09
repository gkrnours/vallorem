from db import db


class Mail(db.Model):
    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    mail = db.Column(db.String(50))

    def __init__(self, mail):
        self.mail = mail
