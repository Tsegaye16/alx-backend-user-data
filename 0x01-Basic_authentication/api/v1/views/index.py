#!/usr/bin/env python3
""" Module for index.py views
"""
from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
    getting the status of pi/v1/status
    and return it's API status
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """
    display the number of objects
    from /api/v1/stats
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def abort_401() -> str:
    """
    display unauthorized endpoint from /api/v1/unauthorized
    """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def abort_403() -> str:
    """
    display forbidden endpoint from /api/vi/forbidden
    """
    abort(403)
