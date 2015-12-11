from vallorem.model.db import Base, engine, db_session
import unittest
from vallorem.model.page import Page


class PageTest(unittest.TestCase):
    def setUp(self):
        Base.metadata.create_all(bind=engine)
        db_session.add(Page(1, 'PageTest', 'Le contenu de la page test'))
        db_session.commit()

    def tearDown(self):
        db_session.drop_all()

    def test_page_exits(self):
        self.assertTrue(Page.query.filter(Page.titre == 'PageTest').first() is not None)

    def test_delete(self):
        page = Page.query.filter(Page.titre == 'PageTest').first()
        page.update_titre('New titre')
        self.assertTrue(Page.query.filter(Page.titre == 'New titre').first() is not None)


