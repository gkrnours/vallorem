# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from sqlalchemy import inspect

from vallorem.test import engine, TestDB
from vallorem.model import db, Base, Equipe


class TestEquipe(TestDB):
    def setUp(self):
        self.e = e = Equipe(nom="dev")
        with db.session() as s:
            s.add(e)


    def tearDown(self):
        Base.metadata.drop_all(bind=db.get_engine())


    def test_create_empty(self):
        e = Equipe()
        with db.session() as s:
            s.add(e)


    def test_create_arg(self):
        e = Equipe(nom="dev")
        with db.session() as s:
            s.add(e)
        self.assertIsInstance(e, Equipe)
        insp = inspect(e)
        self.assertFalse(insp.transient)
        self.assertEqual(e.nom, "dev")


    def test_create_noarg(self):
        e = Equipe()
        e.nom = "dev"
        with db.session() as s:
            s.add(e)
        self.assertIsInstance(e, Equipe)
        insp = inspect(e)
        self.assertFalse(insp.transient)
        self.assertEqual(e.nom, "dev")


    def test_read(self):
        with db.session() as s:
            e = s.query(Equipe).first()
        self.assertIsInstance(e, Equipe)
        self.assertEqual(e.nom, "dev")


    def test_update(self):
        self.assertEqual(self.e.nom, "dev")
        self.e.nom = "user"
        self.assertEqual(self.e.nom, "user")
        with db.session() as s:
            s.add(self.e)
        with db.session() as s:
            e = s.query(Equipe).filter(Equipe.id == self.e.id).first()
        self.assertIsNot(e, self.e)
        self.assertEqual(e.id, self.e.id)
        self.assertEqual(e.nom, "user")


    def test_delete(self):
        with db.session() as s:
            s.delete(self.e)
        insp = inspect(self.e)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            e = s.query(Equipe).filter(Equipe.id == self.e.id).first()
        self.assertIs(e, None)
