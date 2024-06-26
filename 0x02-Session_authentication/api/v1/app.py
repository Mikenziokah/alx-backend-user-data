#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.auth.basic_auth import BasicAuth
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth_type = os.getenv("AUTH_TYPE", None)
if auth_type == 'auth':
    auth = Auth()
if auth_type == "basic_auth":
    auth = BasicAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def not_authorized(error) -> str:
    """
    Not authorized
    """
    return jsonify({"error": "Unauthorized"}), 401


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden() -> str:
    """ GET /api/v1/forbidden
    Return:
      - Aborts
    """
    abort(403)


@app.before_request
def before():
    """
    Before request.
    """
    if auth:
        paths = ['/api/v1/status/',
                 '/api/v1/unauthorized/', '/api/v1/forbidden/',
                 '/api/v1/auth_session/login/']
        if not auth.require_auth(request.path, paths):
            return
        if (not auth.authorization_header(request) and
                not auth.session_cookie(request)):
            abort(401)
        request.current_user = auth.current_user(request)
        if not request.current_user:
            abort(403)


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
