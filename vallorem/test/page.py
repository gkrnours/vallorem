# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import inspect
from vallorem.test import TestDB
from vallorem.model import db, Page, Categorie


class TestPage(TestDB):
    def setUp(self):
        self.c = c = Categorie("Pokémon")
        self.p = p = Page(categorie=c, titre="Pikachu", content="Souris éléc.")
        with db.session() as s:
            s.add(c)
            s.add(p)

    def tearDown(self):
        with db.session() as s:
            s.query(Page).delete()

    def test_create(self):
        # test without argument
        p = Page()
        self.assertIsInstance(p, Page)
        p.categorie = self.c
        p.title = "Marill"
        p.content = "Bleu"
        with db.session() as s:
            s.add(p)
        insp = inspect(p)
        self.assertFalse(insp.transient)
        self.assertEqual(p.categorie, "Pokémon")
        # test with argument
        p = Page(categorie=self.c, titre="Sandslash", content="Pangolin")
        with db.session() as s:
            s.add(p)
        insp = inspect(p)
        self.assertFalse(insp.transient)
        self.assertEqual(p.categorie, "Pokémon")

    def test_without_categorie(self):
        p = Page()
        with db.session() as s:
            s.add(p)

    def test_read(self):
        with db.session() as s:
            p = s.query(Page).first()
        self.assertIsInstance(p, Page)
        self.assertEqual(p.titre, "Pikachu")
        self.assertEqual(p.categorie, "Pokémon")

    def test_update(self):
        self.assertEqual(self.p.content, "Souris éléc.")
        self.p.content = "Souris éléctrique"
        self.assertEqual(self.p.content, "Souris éléctrique")
        with db.session() as s:
            s.add(self.p)
        with db.session() as s:
            p = s.query(Page).filter(Page.id == self.p.id).first()
        self.assertIsNot(p, self.p)
        self.assertEqual(p.id, self.p.id)
        self.assertEqual(p.titre, "Pikachu")
        self.assertEqual(p.content, "Souris éléctrique")

    def test_delete(self):
        with db.session() as s:
            s.delete(self.p)
        insp = inspect(self.p)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            p = s.query(Page).filter(Page.id == self.p.id).first()
        self.assertIs(p, None)
