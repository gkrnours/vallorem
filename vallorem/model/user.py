from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask.ext.login import UserMixin

from vallorem import login_manager
from vallorem.model import db, Base
from vallorem.model.mail import Mail


class User(Base,UserMixin):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    _mail = relationship("Mail", lazy='joined', uselist=False)
    mail_id = Column(Integer, ForeignKey('mail.id'))
    password = Column(String(50))

    @property
    def mail(self):
        return self._mail.mail

    @mail.setter
    def mail(self, value):
        self._mail = value


    @login_manager.user_loader
    def load_user(user_id):
        with db.session() as s:
            return s.query(User).get(int(user_id))
