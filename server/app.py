from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from server.config import Config
from server.extensions import db, migrate, jwt

from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

from server.controllers.auth_controller import auth_bp
from server.controllers.guest_controller import guest_bp
from server.controllers.episode_controller import episode_bp
from server.controllers.appearance_controller import appearance_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("server.config.Config")
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    @app.route("/")
    def index():
        return {"message": "WELCOME TO THE LATE SHOW API!!!"}, 200
    

    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(episode_bp, url_prefix="/")
    app.register_blueprint(guest_bp, url_prefix="/")
    app.register_blueprint(appearance_bp, url_prefix="/")

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(port=5555, debug=True)