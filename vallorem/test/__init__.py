import unittest

import sqlalchemy

from vallorem.model import db


class TestDB(unittest.TestCase):
    """ Setup a temporary database for test """

    @classmethod
    def setUpClass(cls):
        """ init the db """
        engine = db.init(
            engine=sqlalchemy.create_engine('sqlite://'),
            autoflush=True
        )
        db.create(engine)

from vallorem.test.categorie import TestCategorie
