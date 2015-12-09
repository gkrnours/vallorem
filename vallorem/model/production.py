from db import db


class Production(db.Model):
    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    id_type = db.Column(db.Integer, db.ForeignKey('type_production.id'))
    titre = db.Column(db.String(50))
    description = db.Column(db.String(5000))
    extra = db.Column(db.String(500))
    date = db.Column(db.DateTime)

    def __init__(self, id_type, titre, description, extra, date):
        self.id_type = id_type
        self.titre = titre
        self.description = description
        self.extra = extra
        self.date = date
