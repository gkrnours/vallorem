from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from vallorem.model import Base
from vallorem.model.mail import Mail


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    _mail = relationship("Mail", lazy='joined', uselist=False)
    mail_id = Column(Integer, ForeignKey('mail.id'), unique=True)
    password = Column(String(50))

    @property
    def mail(self):
        return self._mail.mail

    @mail.setter
    def mail(self, value):
        self._mail = value
