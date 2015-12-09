from db import db


class Personne(db.Model):
    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    id_statut = db.Column(db.Integer, db.ForeignKey('statut.id'))
    id_equipe = db.Column(db.Integer, db.ForeignKey('equipe.id'))
    nom = db.Column(db.String(50))
    nom_jf = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    date_naissance = db.Column(db.DateTime)
    date_recrutement = db.Column(db.DateTime)
    permanent = db.Column(db.Boolean)

    def __init__(self, id_statut, id_equipe, nom, nom_jf, prenom,
                 date_naissance, date_recrutement, permanent):
        self.id_statut = id_statut
        self.id_equipe = id_equipe
        self.nom = nom
        self.nom_jf = nom_jf
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.date_recrutement = date_recrutement
        self.permanent = permanent
