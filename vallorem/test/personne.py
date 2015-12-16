# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import inspect
from vallorem.test import TestDB
from vallorem.model import db, Personne


class TestPersonne(TestDB):
    def setUp(self):
        self.p = p = Personne(nom="alice")
        with db.session() as s:
            s.add(p)

    def tearDown(self):
        with db.session() as s:
            s.query(Personne).delete()

    def test_create_empty(self):
        p = Personne()
        with db.session() as s:
            s.add(p)

    def test_create_noarg(self):
        p = Personne()
        p.nom = "alice"
        with db.session() as s:
            s.add(p)
        self.assertIsInstance(p, Personne)
        insp = inspect(p)
        self.assertFalse(insp.transient)
        self.assertEqual(p.nom, "alice")

    def test_create_arg(self):
        p = Personne(nom="alice")
        with db.session() as s:
            s.add(p)
        self.assertIsInstance(p, Personne)
        insp = inspect(p)
        self.assertFalse(insp.transient)
        self.assertEqual(p.nom, "alice")

    def test_read(self):
        with db.session() as s:
            p = s.query(Personne).first()
        self.assertIsInstance(p, Personne)
        self.assertEqual(p.nom, "alice")

    def test_update(self):
        self.assertEqual(self.p.nom, "alice")
        self.p.nom = "bob"
        self.assertEqual(self.p.nom, "bob")
        with db.session() as s:
            s.add(self.p)
        with db.session() as s:
            p = s.query(Personne).filter(Personne.id == self.p.id).first()
        self.assertIsNot(p, self.p)
        self.assertEqual(p.id, self.p.id)
        self.assertEqual(p.nom, "bob")

    def test_delete(self):
        with db.session() as s:
            s.delete(self.p)
        insp = inspect(self.p)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            p = s.query(Personne).filter(Personne.id == self.p.id).first()
        self.assertIs(p, None)
