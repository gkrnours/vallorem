# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from sqlalchemy import inspect

from vallorem.test import engine, TestDB
from vallorem.model import db, Base, Mail, User

#TODO test for updating email

class TestUser(TestDB):
    def setUp(self):
        self.m = m = Mail("alice@example.com")
        self.u = u = User(mail=m, password="alice")
        with db.session() as s:
            s.add(m)
            s.add(u)


    def tearDown(self):
        Base.metadata.drop_all(bind=db.get_engine())


    def test_create(self):
        # test without argument
        u = User()
        self.assertIsInstance(u, User)
        u.mail = self.m
        u.password = "bob"
        with db.session() as s:
            s.add(u)
        insp = inspect(u)
        self.assertFalse(insp.transient)
        self.assertEqual(u.mail, "alice@example.com")
        # test with argument
        u = User(mail=self.m, password="bob")
        with db.session() as s:
            s.add(u)
        insp = inspect(u)
        self.assertFalse(insp.transient)
        self.assertEqual(u.mail, "alice@example.com")


    def test_read(self):
        with db.session() as s:
            u = s.query(User).first()
        self.assertIsInstance(u, User)
        self.assertEqual(u.mail, "alice@example.com")
        self.assertEqual(u.password, "alice")


    def test_update(self):
        self.assertEqual(self.u.password, "alice")
        self.u.password = "bob"
        self.assertEqual(self.u.password, "bob")
        with db.session() as s:
            s.add(self.u)
        with db.session() as s:
            u = s.query(User).filter(User.id == self.u.id).first()
        self.assertIsNot(u, self.u)
        self.assertEqual(u.id, self.u.id)
        self.assertEqual(u.password, "bob")
        self.assertEqual(u.mail, "alice@example.com")


    def test_delete(self):
        with db.session() as s:
            s.delete(self.u)
        insp = inspect(self.u)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            u = s.query(User).filter(User.id == self.u.id).first()
        self.assertIs(u, None)
