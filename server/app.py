from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

from server.extensions import db, migrate

app = Flask(__name__)

app.config.from_object("server.config")

db.init_app(app)
migrate.init_app(app, db)