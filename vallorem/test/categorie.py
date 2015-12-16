# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import inspect
from vallorem.test import TestDB
from vallorem.model import db, Categorie


class TestCategorie(TestDB):

    def setUp(self):
        self.c = c = Categorie(description="O'Maley")
        with db.session() as s:
            s.add(c)

    def tearDown(self):
        with db.session() as s:
            s.query(Categorie).delete()

    def test_create_empty(self):
        with self.assertRaises(TypeError):
            c = Categorie()

    def test_create_arg(self):
        c = Categorie(description="O'Maley")
        with db.session() as s:
            s.add(c)
        self.assertIsInstance(c, Categorie)
        insp = inspect(c)
        self.assertFalse(insp.transient)
        self.assertEqual(c.description, "O'Maley")

    def test_read(self):
        # check read
        with db.session() as s:
            c = s.query(Categorie).first()
        self.assertIsInstance(c, Categorie)
        self.assertEqual(c.description, "O'Maley")

    def test_update(self):
        with db.session() as s:
            c = s.query(Categorie).first()
        self.assertIsInstance(c, Categorie)
        self.assertEqual(c.description, "O'Maley")
        c.description = "Pokémon"
        with db.session() as s:
            s.add(c)
        del c
        with db.session() as s:
            c = s.query(Categorie).first()
        self.assertIsInstance(c, Categorie)
        self.assertEqual(c.description, "Pokémon")

    def test_delete(self):
        # get from db
        with db.session() as s:
            c = s.query(Categorie).first()
        self.assertIsInstance(c, Categorie)
        self.assertEqual(c.description, "O'Maley")
        # delete
        with db.session() as s:
            s.delete(c)
        insp = inspect(c)
        self.assertTrue(insp.deleted)
        # check db for survivor
        with db.session() as s:
            c = s.query(Categorie).first()
        self.assertIs(c, None)
        # make a new one for further test
        c = Categorie("O'Maley")
        with db.session() as s:
            s.add(c)


