
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/vuetest'

db = SQLAlchemy(app)

from app import models

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
