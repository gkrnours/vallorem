from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from vallorem.model import Base
from vallorem.model.mail import Mail
from vallorem.model.user_personne import user_personne


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    _mail = relationship("Mail", lazy='joined', uselist=False)
    mail_id = Column(Integer, ForeignKey('mail.id'), unique=True)
    password = Column(String(50))

    personnes = relationship("Personne", secondary=user_personne, back_populates="users")

    @property
    def mail(self):
        return self._mail.mail

    @mail.setter
    def mail(self, value):
        self._mail = value
