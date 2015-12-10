from sqlalchemy import Column, Integer, String
from vallorem.model.db import Base


class Mail(Base):
    __tablename__ = 'mail'
    id = Column(Integer, primary_key=True)
    mail = Column(String(50))

    def __init__(self, mail):
        self.mail = mail
