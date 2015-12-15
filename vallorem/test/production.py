# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from sqlalchemy import inspect

from vallorem.test import engine, TestDB
from vallorem.model import db, Base, Production


class TestProduction(TestDB):
    def setUp(self):
        self.p = p = Production(titre="Influence consommateurs")
        with db.session() as s:
            s.add(p)

    def tearDown(self):
        Base.metadata.drop_all(bind=db.get_engine())

    def test_create_empty(self):
        p = Production()
        with db.session() as s:
            s.add(p)

    def test_create_noarg(self):
        p = Production()
        p.titre = "Influence consommateurs"
        with db.session() as s:
            s.add(p)
        self.assertIsInstance(p, Production)
        insp = inspect(p)
        self.assertFalse(insp.transient)
        self.assertEqual(p.titre, "Influence consommateurs")

    def test_create_arg(self):
        p = Production(titre="Influence consommateurs")
        with db.session() as s:
            s.add(p)
        self.assertIsInstance(p, Production)
        insp = inspect(p)
        self.assertFalse(insp.transient)
        self.assertEqual(p.titre, "Influence consommateurs")

    def test_read(self):
        with db.session() as s:
            p = s.query(Production).first()
        self.assertIsInstance(p, Production)
        self.assertEqual(p.titre, "Influence consommateurs")

    def test_update(self):
        self.assertEqual(self.p.titre, "Influence consommateurs")
        self.p.titre = "consommateurs"
        self.assertEqual(self.p.titre, "consommateurs")
        with db.session() as s:
            s.add(self.p)
        with db.session() as s:
            p = s.query(Production).filter(Production.id == self.p.id).first()
        self.assertIsNot(p, self.p)
        self.assertEqual(p.id, self.p.id)
        self.assertEqual(p.titre, "consommateurs")

    def test_delete(self):
        with db.session() as s:
            s.delete(self.p)
        insp = inspect(self.p)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            p = s.query(Production).filter(Production.id == self.p.id).first()
        self.assertIs(p, None)
