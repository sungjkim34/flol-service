from flask import (
    Blueprint,
    jsonify,
    current_app as app
)

flol_auth_api = Blueprint('flol_auth', __name__)

@flol_auth_api.route('/auth/login', methods=['POST'])
def login():
    return jsonify({})


@flol_auth_api.route('/auth/signup', methods=['POST'])
def signup():
    return jsonify({})


@flol_auth_api.route('/auth/logout', methods=['POST'])
def logout():
    return jsonify({})
