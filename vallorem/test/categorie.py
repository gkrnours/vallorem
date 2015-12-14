# -*- encoding: utf-8 -*-

from sqlalchemy import inspect

from vallorem.test import TestDB
from vallorem.model import db, Categorie

class TestCategorie(TestDB):

    def test_create(self):
        # check that creation without arg fail
        with self.assertRaises(TypeError):
            Categorie()
        # check creation and insert in db
        c = Categorie("O'Maley")
        with db.session() as s:
            s.add(c)
        insp = inspect(c)
        self.assertFalse(insp.transient)

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
        c.description = u"Pokémon"
        with db.session() as s:
            s.add(c)
        del c
        with db.session() as s:
            c = s.query(Categorie).first()
        self.assertIsInstance(c, Categorie)
        self.assertEqual(c.description, u"Pokémon")

    def test_delete(self):
        # get from db
        with db.session() as s:
            c = s.query(Categorie).first()
        self.assertIsInstance(c, Categorie)
        self.assertEqual(c.description, u"O'Maley")
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


