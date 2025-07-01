from .extensions import db

from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password_hash = db.Column(db.String, nullable=False)


    @property
    def password(self):
        raise AttributeError("Password is write-only.")
    
    @password.setter
    def password(self, plain_password):
        self.password_hash = generate_password_hash(plain_password)


    def check_password(self, plain_password):
        return check_password_hash(self.password_hash, plain_password)
    

    def __repr__(self):
        return f"<User {self.id}: {self.username}>"