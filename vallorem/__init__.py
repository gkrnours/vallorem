from flask import Flask

USERNAME = "root"
PASSWORD = "root"
DATABASE = "sqlite:///db/vallorem.db"
SECRET_KEY = "dev key"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar("VALLOREM_SETTINGS", silent=True)

from vallorem import views
from vallorem.model import db


def start(**kwargs):
    db.init()
    app.run(**kwargs)
