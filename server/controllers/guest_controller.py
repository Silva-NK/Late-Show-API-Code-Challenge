from flask import Blueprint, jsonify

from server.extensions import db

from server.models.guest import Guest