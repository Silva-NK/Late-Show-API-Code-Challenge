from flask_restful import Api, Resource
from flask import Blueprint, jsonify, make_response

from ..models.extensions import db

from ..models.guest import Guest

guest_bp = Blueprint("guests", __name__)
guest_api = Api(guest_bp)

class GuestsAPI(Resource):
    def get(self):
        guests = []

        for guest in Guest.query.all():
            guest_dict = guest.to_dict()
            guests.append(guest_dict)

        response = make_response(
            guests,
            200,
            {"Content-Type": "application/json"}
        )

        return response
    

guest_api.add_resource(GuestsAPI, "/guests")