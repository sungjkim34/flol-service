from flask import (
    Blueprint,
    jsonify,
    current_app as app
)

flol_user_api = Blueprint('flol_user', __name__)

@flol_user_api.route('/user', methods=['GET'])
def get_my_user_info():
    # return user information
    # username, follower count, following count, bio, etc
    return jsonify({})


@flol_user_api.route('/user/<user_id>', methods=['GET'])
def get_user_info(user_id):
    # return user information
    # username, follower count, following count, bio, etc
    return jsonify({})


@flol_user_api.route('/user/followers', methods=['GET'])
def get_user_followers():
    # return followers
    return jsonify({})


@flol_user_api.route('/user/following', methods=['GET'])
def get_user_followers():
    # return following
    return jsonify({})


@flol_user_api.route('/user/<user_id>/follow', methods=['PUT'])
def follow_user():
    # folllow user
    return jsonify({})


@flol_user_api.route('/user/<user_id>/follow', methods=['DELETE'])
def unfollow_user():
    # unfolllow user
    return jsonify({})
