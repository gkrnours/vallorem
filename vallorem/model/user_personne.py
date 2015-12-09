from db import db


class UserPersonne(db.Model):
    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_personne = db.Column(db.Integer, db.ForeignKey('personne.id'))

    def __init__(self, id_user, id_personne):
        self.is_user = id_user
        self.id_personne = id_personne
