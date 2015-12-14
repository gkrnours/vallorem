import unittest

import sqlalchemy

from vallorem.model import db

engine = None


class TestDB(unittest.TestCase):
    """ Setup a temporary database for test """

    @classmethod
    def setUpClass(cls):
        """ init the db """
        global engine
        engine = sqlalchemy.create_engine('sqlite://')
        engine = db.init(engine=engine, autoflush=True)
        db.create(engine)

from vallorem.test.categorie import TestCategorie
from vallorem.test.mail import TestMail
from vallorem.test.page import TestPage
from vallorem.test.personne import TestPersonne
from vallorem.test.statut import TestStatut
from vallorem.test.user import TestUser
