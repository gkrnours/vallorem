import unittest

import sqlalchemy

from vallorem.model import db

engine = None

class TestDB(unittest.TestCase):
    """ Setup a temporary database for test """
    engine = None

    @classmethod
    def setUpClass(cls):
        """ init the db """
        cls.engine = engine =  sqlalchemy.create_engine('sqlite://')
        engine = db.init(engine=engine, autoflush=True)
        db.create(engine)

from vallorem.test.categorie import TestCategorie
from vallorem.test.equipe import TestEquipe
from vallorem.test.mail import TestMail
from vallorem.test.page import TestPage
from vallorem.test.personne import TestPersonne
from vallorem.test.statut import TestStatut
from vallorem.test.user import TestUser
from vallorem.test.doctorant import TestDoctorant
from vallorem.test.production import TestProduction
from vallorem.test.type_production import TestTypeProduction
from vallorem.test.observation import TestObservation
from vallorem.test.type_financement import TestTypeFinancement
from vallorem.test.chg_equipe import TestChgEquipe
from vallorem.test.date_promotion import TestDatePromotion