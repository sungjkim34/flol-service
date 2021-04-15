from flask import (
    Blueprint,
    jsonify,
    current_app as app
)

flol_event_api = Blueprint('flol_event', __name__)

@flol_event_api.route('/event/<event_id>', methods=['GET'])
def get_event(event_id):
    return jsonify({})