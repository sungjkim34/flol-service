from flask import (
    Blueprint,
    jsonify,
    current_app as app
)

flol_event_api = Blueprint('flol_event', __name__)

@flol_event_api.route('/event/<event_id>', methods=['GET'])
def get_event(event_id):
    return jsonify({})


@flol_event_api.route('/event', methods=['GET'])
def get_events():
    # get all events for user followers
    return jsonify({})


@flol_event_api.route('/event', methods=['POST'])
def create_event():
    return jsonify({})


@flol_event_api.route('/event/<event_id>', methods=['PUT'])
def update_event(event_id):
    return jsonify({})


@flol_event_api.route('/event/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    return jsonify({})
