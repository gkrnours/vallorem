# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy.exc import IntegrityError
from sqlalchemy import inspect
from vallorem.test import TestDB
from vallorem.model import db, Doctorant, Personne


class TestDoctorant(TestDB):
    def setUp(self):
        self.p = p = Personne(nom="Doctorant")
        self.d = d = Doctorant(sujet_these="alice", personne=p)
        with db.session() as s:
            s.add(p)
            s.add(d)

    def tearDown(self):
        with db.session() as s:
            s.query(Doctorant).delete()
            s.query(Personne).delete()

    def test_create_noarg(self):
        d = Doctorant()
        d.sujet_these = "alice"
        d.personne = p = Personne(nom="alice")
        with db.session() as s:
            s.add(p)
            s.add(d)
        self.assertIsInstance(d, Doctorant)
        insp = inspect(d)
        self.assertFalse(insp.transient)
        self.assertEqual(d.sujet_these, "alice")

    def test_create_arg(self):
        p = Personne(nom="alice")
        d = Doctorant(personne=p, sujet_these="alice")
        with db.session() as s:
            s.add(d)
        self.assertIsInstance(d, Doctorant)
        insp = inspect(d)
        self.assertFalse(insp.transient)
        self.assertEqual(d.sujet_these, "alice")

    def test_insert_empty(self):
        # test with argument
        d = Doctorant()
        with self.assertRaises(IntegrityError):
            with db.session() as s:
                s.add(d)

    def test_unique(self):
        d = Doctorant(personne=self.p, sujet_these="alice")
        with self.assertRaises(IntegrityError):
            with db.session() as s:
                s.add(d)

    def test_getter_tf(self):
        d = Doctorant()
        self.assertIsNone(d.type_financement)

    def test_getter_obs(self):
        d = Doctorant()
        self.assertIsNone(d.observation)

    def test_read(self):
        with db.session() as s:
            d = s.query(Doctorant).first()
        self.assertIsInstance(d, Doctorant)
        self.assertEqual(d.sujet_these, "alice")

    def test_update(self):
        self.assertEqual(self.d.sujet_these, "alice")
        self.d.sujet_these = "bob"
        self.assertEqual(self.d.sujet_these, "bob")
        with db.session() as s:
            s.add(self.d)
        with db.session() as s:
            d = s.query(Doctorant).filter(Doctorant.id == self.d.id).first()
        self.assertIsNot(d, self.d)
        self.assertEqual(d.id, self.d.id)
        self.assertEqual(d.sujet_these, "bob")

    def test_delete(self):
        with db.session() as s:
            s.delete(self.d)
        insp = inspect(self.d)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            d = s.query(Doctorant).filter(Doctorant.id == self.d.id).first()
        self.assertIs(d, None)
