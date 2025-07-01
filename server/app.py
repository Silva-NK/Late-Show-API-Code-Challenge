import os

from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .models.extensions import db, migrate, jwt

from .models.user import User
from .models.guest import Guest
from .models.episode import Episode
from .models.appearance import Appearance

from .controllers.auth_controller import auth_bp
from .controllers.guest_controller import guest_bp
from .controllers.episode_controller import episode_bp
from .controllers.appearance_controller import appearance_bp

from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_COMPACT'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600))
    
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