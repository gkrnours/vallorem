import unittest
from vallorem.model.personne import Personne
from vallorem import app
from vallorem.model.db import db
from datetime import date, datetime
import flask.ext.testing

class personneTestCase(unittest.TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_add(self):
        now = datetime.now()
        personne = Personne(12,34,'PUYO',None,'Puyo', now.date(), date(2000,1,1), True)
        db.session.add(personne)
        db.session.commit()

        assert personne in db.session

        response = self.client.get("/")

        assert personne in db.session


