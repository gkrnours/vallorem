import unittest
from personne import Personne
from db import db
from datetime import date, datetime
import flask.ext.testing

class personneTestCase(unittest.TestCase):



    def test_add(self):
        now = datetime.now()
        personne = Personne(12,34,'PUYO',None,'Puyo', now.date(), date(2000,1,1), True)
        db.session.add(personne)
        db.session.commit()

        assert personne in db.session

        response = self.client

        assert personne in db.session


if __name__ == '__main__':
    unittest.main()