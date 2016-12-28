
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask_debugtoolbar import DebugToolbarExtension
import logging
from logging.handlers import RotatingFileHandler


app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)


# the toolbar is only enabled in debug mode:
app.debug = True
toolbar = DebugToolbarExtension(app)


handler = RotatingFileHandler('foo.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)


from app import models, views

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
