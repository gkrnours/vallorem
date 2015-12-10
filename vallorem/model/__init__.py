from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from vallorem.model.categorie import Categorie
from vallorem.model.chg_equipe import ChgEquipe
from vallorem.model.date_promotion import DatePromotion
from vallorem.model.directeur_these import DirecteurThese
from vallorem.model.doctorant import Doctorant
from vallorem.model.equipe import Equipe
from vallorem.model.mail import Mail
from vallorem.model.mail_personne import MailPersonne
from vallorem.model.observation import Observation
from vallorem.model.page import Page
from vallorem.model.personne import Personne
from vallorem.model.production import Production
from vallorem.model.production_personne import ProductionPersonne
from vallorem.model.statut import Statut
from vallorem.model.type_financement import TypeFinancement
from vallorem.model.type_production import TypeProduction
from vallorem.model.user import User
from vallorem.model.user_personne import UserPersonne

