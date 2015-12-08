from flask import Flask
from flask.sqlalchemy import SQLAlchemy
from vallorem import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../vallorem.db'
db = SQLAlchemy(app)

