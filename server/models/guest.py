from sqlalchemy_serializer import SerializerMixin

from .extensions import db

class Guest(db.Model, SerializerMixin):
    __tablename__ = "guests"

    serialize_rules = ('-appearances.guest', 'appearances')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String, nullable=False)

    appearances = db.relationship('Appearance', back_populates="guest", cascade="all, delete-orphan")


    def __repr__(self):
        return f"<Guest {self.id}: {self.name}, {self.occupation}>"