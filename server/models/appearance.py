from sqlalchemy.orm import validates
from sqlalchemy import CheckConstraint
from sqlalchemy_serializer import SerializerMixin

from extensions import db

class Appearance(db.Model, SerializerMixin):
    __tablename__ = "appearances"

    serialize_rules = ('-episode.appearances', '-guest.appearances')

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id', ondelete="CASCADE"), nullable=False)

    guest = db.relationship('Guest', back_populates="appearances")
    episode = db.relationship('Episode', back_populates="appearances")

    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )

    @validates('rating')
    def validate_rating(self, key, value):
        if not (1 <= value <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")
        return value


    def __repr__(self):
        return f"<Appearance {self.id} | Episode: {self.episode.number} | Guest: {self.guest.name} | Rating: {self.rating}>"