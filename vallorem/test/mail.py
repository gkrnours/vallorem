# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

from sqlalchemy import inspect

from vallorem.test import engine, TestDB
from vallorem.model import db, Base, Mail

class TestMail(TestDB):
    def setUp(self):
        self.m = m = Mail("abc@example.com")
        with db.session() as s:
            s.add(m)


    def tearDown(self):
        Base.metadata.drop_all(bind=db.get_engine())


    def test_create(self):
        # test without argument
        with self.assertRaises(TypeError):
            Mail()
        # test with argument
        m = Mail("def@example.com")
        with db.session() as s:
            s.add(m)
        insp = inspect(m)
        self.assertFalse(insp.transient)


    def test_read(self):
        with db.session() as s:
            m = s.query(Mail).first()
        self.assertIsInstance(m, Mail)
        self.assertEqual(m.mail, "abc@example.com")


    def test_update(self):
        self.assertEqual(self.m.mail, "abc@example.com")
        self.m.mail = "def@example.com"
        self.assertEqual(self.m.mail, "def@example.com")
        with db.session() as s:
            s.add(self.m)
        with db.session() as s:
            m = s.query(Mail).filter(Mail.id == self.m.id).first()
        self.assertIsNot(m, self.m)
        self.assertEqual(m.id, self.m.id)
        self.assertEqual(m.mail, "def@example.com")


    def test_delete(self):
        with db.session() as s:
            s.delete(self.m)
        insp = inspect(self.m)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            m = s.query(Mail).filter(Mail.id == self.m.id).first()
        self.assertIs(m, None)
