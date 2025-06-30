from sqlalchemy_serializer import SerializerMixin

from extensions import db

class Episode(db.Model, SerializerMixin):
    __tablename__ = "episodes"

    serialize_rules = ('appearances', '-appearances.episode')

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    number = db.Column(db.Integer, nullable=False, unique=True)

    appearances = db.relationship('Appearance', back_populates="episode", cascade='all, delete-orphan')

    
    def __repr__(self):
        return f"<Episode {self.id}: #{self.number}, {self.date.strftime('%Y-%m-%d')}>"