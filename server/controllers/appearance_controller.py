from flask import Blueprint, request
from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required

from models.extensions import db

from models.guest import Guest
from models.episode import Episode
from models.appearance import Appearance

appearance_bp = Blueprint("appearance", __name__)
appearance_api = Api(appearance_bp)

class CreateAppearanceAPI(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        rating = data.get("rating")
        guest_id = data.get("guest_id")
        episode_id = data.get("episode_id")

        if not all([rating, guest_id, episode_id]):
            return {"error": "rating, guest_id, and episode_id are required."}, 400
        
        guest = Guest.query.get(guest_id)
        if not guest:
            return {"error": "Guest not found."}, 404
        
        episode = Episode.query.get(episode_id)
        if not episode:
            return {"error": "Episode not found."}, 404
        
        try:
            appearance = Appearance(
                rating=rating,
                guest_id=guest_id,
                episode_id=episode_id
            )
            db.session.add(appearance)
            db.session.commit()
        except ValueError as ve:
            return {"error": str(ve)}, 400
        
        return appearance.to_dict(), 201
    

appearance_api.add_resource(CreateAppearanceAPI, "/appearances")