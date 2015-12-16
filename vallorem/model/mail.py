from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from vallorem.model import Base
from vallorem.model.mail_personne import mail_personne


class Mail(Base):
    __tablename__ = 'mail'
    id = Column(Integer, primary_key=True)
    mail = Column(String(50), unique=True)

    personnes = relationship("Personne", secondary=mail_personne, back_populates="mails")

    def __init__(self, mail):
        self.mail = mail
