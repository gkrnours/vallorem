# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import inspect
from vallorem.test import TestDB
from vallorem.model import db, Doctorant


class TestDoctorant(TestDB):
    def setUp(self):
        self.d = d = Doctorant(sujet_these="alice")
        with db.session() as s:
            s.add(d)

    def tearDown(self):
        with db.session() as s:
            s.query(Doctorant).delete()

    def test_create_empty(self):
        d = Doctorant()
        with db.session() as s:
            s.add(d)

    def test_create_noarg(self):
        d = Doctorant()
        d.sujet_these = "alice"
        with db.session() as s:
            s.add(d)
        self.assertIsInstance(d, Doctorant)
        insp = inspect(d)
        self.assertFalse(insp.transient)
        self.assertEqual(d.sujet_these, "alice")

    def test_create_arg(self):
        d = Doctorant(sujet_these="alice")
        with db.session() as s:
            s.add(d)
        self.assertIsInstance(d, Doctorant)
        insp = inspect(d)
        self.assertFalse(insp.transient)
        self.assertEqual(d.sujet_these, "alice")

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
