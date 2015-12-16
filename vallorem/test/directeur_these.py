# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from vallorem.test import TestDB
from vallorem.model import db, Personne, DirecteurThese


class TestDirecteurThese(TestDB):
    def setUp(self):
        self.pu = pu = Personne(nom="DocUpdate")
        self.pa = pa = Personne(nom="directeur")
        self.pb = pb = Personne(nom="doctorant")
        self.dt = dt = DirecteurThese(directeur=pa, doctorant=pb)
        with db.session() as s:
            s.add(pa)
            s.add(pb)
            s.add(dt)
            s.add(pu)

    def tearDown(self):
        with db.session() as s:
            s.query(Personne).delete()
            s.query(Personne).delete()
            s.query(DirecteurThese).delete()

    def test_create_noarg(self):
        # test without argument
        dt = DirecteurThese()
        dt.directeur = self.pa
        dt.doctorant = self.pb
        with db.session() as s:
            s.add(dt)
        insp = inspect(dt)
        self.assertFalse(insp.transient)
        self.assertEqual(dt.directeur.id, self.pa.id)
        self.assertEqual(dt.doctorant.id, self.pb.id)

    def test_create_arg(self):
        dt = DirecteurThese(directeur=self.pa, doctorant=self.pb)
        with db.session() as s:
            s.add(dt)
        insp = inspect(dt)
        self.assertFalse(insp.transient)
        self.assertEqual(dt.directeur.id, self.pa.id)
        self.assertEqual(dt.doctorant.id, self.pb.id)

    def test_read(self):
        with db.session() as s:
            dt = s.query(DirecteurThese).first()
        self.assertIsInstance(dt, DirecteurThese)
        self.assertEqual(dt.directeur.id, self.pa.id)
        self.assertEqual(dt.doctorant.id, self.pb.id)

    def test_update(self):

        self.assertEqual(self.dt.doctorant, self.pb)
        self.dt.doctorant = self.pu
        self.assertEqual(self.dt.doctorant.id, self.pu.id)
        with db.session() as s:
            s.add(self.dt)
        with db.session() as s:
            dt = s.query(DirecteurThese).filter(DirecteurThese.id == self.dt.id).first()
        self.assertIsNot(dt, self.dt)
        self.assertEqual(dt.id, self.dt.id)
        self.assertEqual(dt.doctorant.id, self.pu.id)
        self.assertEqual(dt.directeur.id, self.pa.id)

    def test_delete(self):
        with db.session() as s:
            s.delete(self.dt)
        insp = inspect(self.dt)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            dt = s.query(DirecteurThese).filter(DirecteurThese.id == self.dt.id).first()
        self.assertIs(dt, None)
