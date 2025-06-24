from flask_restful import Api, Resource
from flask_jwt_extended import jwt_required
from flask import Blueprint, jsonify, make_response

from server.extensions import db

from server.models.episode import Episode

episode_bp = Blueprint("episodes", __name__)
episode_api = Api(episode_bp)

class AllEpisodesAPI(Resource):
    def get(self):
        episodes = []

        for episode in Episode.query.all():
            episode_dict = episode.to_dict()
            episodes.append(episode_dict)

        response = make_response(
            episodes,
            200,
            {"Content-Type": "application/JSON"}
        )
    
        return response
    

class EpisodeAPI(Resource):
    def get(self, id):
        episode = Episode.query.filter(Episode.id == id).first()
        if not episode:
            return {"error": "Episode not found"}, 404
        
        episode_dict = episode.to_dict()

        response = make_response(
            episode_dict,
            200
        )

        return response
    
    @jwt_required()
    def delete(self, id):
        episode = Episode.query.filter(Episode.id == id).first()
        if not episode:
            return {"error": "Episode not found"}, 404
        
        db.session.delete(episode)
        db.session.commit()

        return {"message": f"Episode {id} deleted"}, 200
    

episode_api.add_resource(AllEpisodesAPI, "/episodes")
episode_api.add_resource(EpisodeAPI, "/episodes/<int:id>")