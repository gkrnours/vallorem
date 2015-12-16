# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import inspect
from vallorem.test import TestDB
from vallorem.model import db, TypeFinancement


class TestTypeFinancement(TestDB):
    def setUp(self):
        self.tf = tf = TypeFinancement(description="alice")
        with db.session() as s:
            s.add(tf)

    def tearDown(self):
        with db.session() as s:
            s.query(TypeFinancement).delete()

    def test_create_empty(self):
        with self.assertRaises(TypeError):
            TypeFinancement()

    def test_create_arg(self):
        tf = TypeFinancement(description="alice")
        with db.session() as s:
            s.add(tf)
        self.assertIsInstance(tf, TypeFinancement)
        insp = inspect(tf)
        self.assertFalse(insp.transient)
        self.assertEqual(tf.description, "alice")

    def test_read(self):
        with db.session() as s:
            tf = s.query(TypeFinancement).first()
        self.assertIsInstance(tf, TypeFinancement)
        self.assertEqual(tf.description, "alice")

    def test_update(self):
        self.assertEqual(self.tf.description, "alice")
        self.tf.description = "bob"
        self.assertEqual(self.tf.description, "bob")
        with db.session() as s:
            s.add(self.tf)
        with db.session() as s:
            tf = s.query(TypeFinancement).filter(TypeFinancement.id == self.tf.id).first()
        self.assertIsNot(tf, self.tf)
        self.assertEqual(tf.id, self.tf.id)
        self.assertEqual(tf.description, "bob")

    def test_delete(self):
        with db.session() as s:
            s.delete(self.tf)
        insp = inspect(self.tf)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            tf = s.query(TypeFinancement).filter(TypeFinancement.id == self.tf.id).first()
        self.assertIs(tf, None)
