from flask import Flask

USERNAME = "root"
PASSWORD = "root"
DATABASE = "vallorem.db"
SECRET_KEY = "dev key"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar("VALLOREM_SETTINGS", silent=True)

import vallorem.views
