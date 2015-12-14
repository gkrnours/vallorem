from flask import Flask
from flask.ext.login import LoginManager

USERNAME = "root"
PASSWORD = "root"
DATABASE = "sqlite:///db/vallorem.db"
SECRET_KEY = "dev key"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar("VALLOREM_SETTINGS", silent=True)

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

import vallorem.views
