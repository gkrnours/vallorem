from vallorem.model.db import db


class Equipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    axe = db.Column(db.String(50))
    localisation = db.Column(db.String(40))

    def __init__(self, nom, axe, localisation):
        self.nom = nom
        self.axe = axe
        self.localisation = localisation
