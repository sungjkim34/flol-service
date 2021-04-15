import os

from flask import Flask
from flask.json import JSONEncoder
# from flask_cors import CORS

# from flol.log import configure_logger

from flol.routes.event import flol_event_api


def get_config_file(env):
    """
    Return a path to a config file based on the environment
    """
    return f'config/config_{env.lower()}.py'
    

def create_app():
    """
    Main function to create the Flask app, configure X-Ray, and register the
    routes, error handlers, and rq workers.
    """
    flask_app = Flask(__name__)
    # CORS(flask_app, supports_credentials=True)

    env = os.environ.get('FLASK_ENV', 'local')
    flask_app.config.from_pyfile(get_config_file(env))

    flask_app.register_blueprint(flol_event_api)

    # from flol.error_handler import register_error_handlers
    # register_error_handlers(flask_app)

    return flask_app


app = create_app()
app.config['EXECUTOR_PROPAGATE_EXCEPTIONS'] = True


# @app.before_first_request
# def setup_logging():
#     if not app.debug:
#         configure_logger(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8443)
