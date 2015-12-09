from db import db


class MailPersonne(db.Model):
    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    id_personne = db.Column(db.Integer, db.ForeignKey('personne.id'))
    id_mail = db.Column(db.Integer, db.ForeignKey('mail.id'))

    def __init__(self, id_personne, id_mail):
        self.id_personne = id_personne
        self.id_mail = id_mail
