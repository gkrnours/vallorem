# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from sqlalchemy import inspect

from vallorem.test import engine, TestDB
from vallorem.model import db, Base, Statut


class TestStatut(TestDB):
    def setUp(self):
        self.st = st = Statut(description="dev")
        with db.session() as s:
            s.add(st)


    def tearDown(self):
        Base.metadata.drop_all(bind=db.get_engine())


    def test_create_empty(self):
        with self.assertRaises(TypeError):
            st = Statut()


    def test_create_arg(self):
        st = Statut(description="dev")
        with db.session() as s:
            s.add(st)
        self.assertIsInstance(st, Statut)
        insp = inspect(st)
        self.assertFalse(insp.transient)
        self.assertEqual(st.description, "dev")


    def test_read(self):
        with db.session() as s:
            st = s.query(Statut).first()
        self.assertIsInstance(st, Statut)
        self.assertEqual(st.description, "dev")


    def test_update(self):
        self.assertEqual(self.st.description, "dev")
        self.st.description = "user"
        self.assertEqual(self.st.description, "user")
        with db.session() as s:
            s.add(self.st)
        with db.session() as s:
            st = s.query(Statut).filter(Statut.id == self.st.id).first()
        self.assertIsNot(st, self.st)
        self.assertEqual(st.id, self.st.id)
        self.assertEqual(st.description, "user")


    def test_delete(self):
        with db.session() as s:
            s.delete(self.st)
        insp = inspect(self.st)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            st = s.query(Statut).filter(Statut.id == self.st.id).first()
        self.assertIs(st, None)
