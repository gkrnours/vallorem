# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from sqlalchemy import inspect

from vallorem.test import engine, TestDB
from vallorem.model import db, Base, TypeProduction


class TestTypeProduction(TestDB):
    def setUp(self):
        self.tp = tp = TypeProduction(description="alice", publication=False)
        with db.session() as s:
            s.add(tp)


    def tearDown(self):
        Base.metadata.drop_all(bind=db.get_engine())


    def test_create_empty(self):
        with self.assertRaises(TypeError):
            TypeProduction()


    def test_create_arg(self):
        tp = TypeProduction(description="alice", publication=False)
        with db.session() as s:
            s.add(tp)
        self.assertIsInstance(tp, TypeProduction)
        insp = inspect(tp)
        self.assertFalse(insp.transient)
        self.assertEqual(tp.description, "alice")


    def test_read(self):
        with db.session() as s:
            tp = s.query(TypeProduction).first()
        self.assertIsInstance(tp, TypeProduction)
        self.assertEqual(tp.description, "alice")


    def test_update(self):
        self.assertEqual(self.tp.description, "alice")
        self.assertEqual(self.tp.publication, False)
        self.tp.description = "bob"
        self.tp.publication = True
        self.assertEqual(self.tp.description, "bob")
        self.assertEqual(self.tp.publication, True)
        with db.session() as s:
            s.add(self.tp)
        with db.session() as s:
            tp = s.query(TypeProduction).filter(TypeProduction.id == self.tp.id).first()
        self.assertIsNot(tp, self.tp)
        self.assertEqual(tp.id, self.tp.id)
        self.assertEqual(tp.description, "bob")
        self.assertEqual(tp.publication, True)


    def test_delete(self):
        with db.session() as s:
            s.delete(self.tp)
        insp = inspect(self.tp)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            tp = s.query(TypeProduction).filter(TypeProduction.id == self.tp.id).first()
        self.assertIs(tp, None)
