from vallorem.model.db import db


class Observation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(500))

    def __init__(self, description):
        self.description = description
