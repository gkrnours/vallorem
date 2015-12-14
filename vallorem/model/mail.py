from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from vallorem.model import Base


class Mail(Base):
    __tablename__ = 'mail'
    id = Column(Integer, primary_key=True)
    mail = Column(String(50))

    def __init__(self, mail):
        self.mail = mail
