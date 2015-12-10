from flask.ext.testing import TestCase
from vallorem import app
from vallorem.model.db import db

class MyTest(TestCase):

    TESTING = True

    def create_app(self):

        # pass in test configuration
        return app

    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()