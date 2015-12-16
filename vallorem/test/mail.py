# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from vallorem.test import TestDB
from vallorem.model import db, Mail

class TestMail(TestDB):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.m = m = Mail("abc@example.com")
        with db.session() as s:
            s.add(m)


    def tearDown(self):
        with db.session() as s:
            s.query(Mail).delete()


    def test_create_noarg(self):
        with self.assertRaises(TypeError):
            Mail()

    def test_create_arg(self):
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

    def test_unique(self):
        m = Mail("abc@example.com")
        with self.assertRaises(IntegrityError):
            with db.session() as s:
                  s.add(m)

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

