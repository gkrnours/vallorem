from db import db


class TypeFinancement(db.Model):
    id = db.Column(db.Integer, primary_key=True, sqlite_autoincrement=True)
    description = db.Column(db.String(50))

    def __init__(self, description):
        self.description = description
