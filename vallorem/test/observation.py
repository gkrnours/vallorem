# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from sqlalchemy import inspect

from vallorem.test import engine, TestDB
from vallorem.model import db, Base, Observation


class TestObservation(TestDB):
    def setUp(self):
        self.o = o = Observation(description="alice")
        with db.session() as s:
            s.add(o)


    def tearDown(self):
        Base.metadata.drop_all(bind=db.get_engine())


    def test_create(self):
        o = Observation(description="alice")
        with db.session() as s:
            s.add(o)
        self.assertIsInstance(o, Observation)
        insp = inspect(o)
        self.assertFalse(insp.transient)
        self.assertEqual(o.description, "alice")


    def test_read(self):
        with db.session() as s:
            o = s.query(Observation).first()
        self.assertIsInstance(o, Observation)
        self.assertEqual(o.description, "alice")


    def test_update(self):
        self.assertEqual(self.o.description, "alice")
        self.o.description = "bob"
        self.assertEqual(self.o.description, "bob")
        with db.session() as s:
            s.add(self.o)
        with db.session() as s:
            o = s.query(Observation).filter(Observation.id == self.o.id).first()
        self.assertIsNot(o, self.o)
        self.assertEqual(o.id, self.o.id)
        self.assertEqual(o.description, "bob")


    def test_delete(self):
        with db.session() as s:
            s.delete(self.o)
        insp = inspect(self.o)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            o = s.query(Observation).filter(Observation.id == self.o.id).first()
        self.assertIs(o, None)
