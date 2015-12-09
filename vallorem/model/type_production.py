from vallorem.model.db import db


class TypeProduction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500))
    publication = db.Column(db.Boolean)

    def __init__(self, description, publication):
        self.description = description
        self.publication = publication
