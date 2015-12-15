# -*- encoding: utf-8 -*-

from sqlalchemy import inspect
from datetime import datetime
from vallorem.test import TestDB
from vallorem.model import db, DatePromotion, Base

class TestDatePromotion(TestDB):

    def setUp(self):
        self.ce = ce = DatePromotion(date_promotion=datetime(2000,1,1))
        with db.session() as s:
            s.add(ce)


    def tearDown(self):
        Base.metadata.drop_all(bind=db.get_engine())

    def test_create_empty(self):
        ce = DatePromotion()
        with db.session() as s:
            s.add(ce)


    def test_create_noarg(self):
        ce = DatePromotion()
        ce.date_promotion = datetime(2000,1,1)
        with db.session() as s:
            s.add(ce)
        self.assertIsInstance(ce, DatePromotion)
        insp = inspect(ce)
        self.assertFalse(insp.transient)
        self.assertEqual(ce.date_promotion, datetime(2000,1,1))


    def test_create_arg(self):
        ce = DatePromotion(date_promotion=datetime(2000,1,1))
        with db.session() as s:
            s.add(ce)
        self.assertIsInstance(ce, DatePromotion)
        insp = inspect(ce)
        self.assertFalse(insp.transient)
        self.assertEqual(ce.date_promotion, datetime(2000,1,1))


    def test_read(self):
        with db.session() as s:
            ce = s.query(DatePromotion).first()
        self.assertIsInstance(ce, DatePromotion)
        self.assertEqual(ce.date_promotion, datetime(2000,1,1))


    def test_update(self):
        self.assertEqual(self.ce.date_promotion, datetime(2000,1,1))
        self.ce.date_promotion = datetime(2015,1,1)
        self.assertEqual(self.ce.date_promotion, datetime(2015,1,1))
        with db.session() as s:
            s.add(self.ce)
        with db.session() as s:
            ce = s.query(DatePromotion).filter(DatePromotion.id == self.ce.id).first()
        self.assertIsNot(ce, self.ce)
        self.assertEqual(ce.id, self.ce.id)
        self.assertEqual(ce.date_promotion, datetime(2015,1,1))


    def test_delete(self):
        with db.session() as s:
            s.delete(self.ce)
        insp = inspect(self.ce)
        self.assertTrue(insp.deleted)
        with db.session() as s:
            ce = s.query(DatePromotion).filter(DatePromotion.id == self.ce.id).first()
        self.assertIs(ce, None)
