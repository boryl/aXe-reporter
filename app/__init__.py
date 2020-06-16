'''
    File name: __init__.py
    Project: aXe reporter
    Author: Björn-Olle Rylander
    Date created: 2019-07-07
    Python Version: 3.7.4
    Description: App init
'''

import os
from flask import Flask


def create_app():
    app = Flask(__name__)

    # Config
    os.environ['FLASK_ENV'] = "development"
    app.config.from_object('config.' + os.getenv('FLASK_ENV'))

    with app.app_context():
        # Routes
        from . import routes
        from . import errors

        # CLI
        from . import cli
        app.cli.add_command(cli.axe_cli)

        # Blueprints
        app.register_blueprint(routes.main_bp)

        # Error handlers
        app.register_error_handler(404, errors.page_not_found)
        app.register_error_handler(400, errors.bad_request)
        app.register_error_handler(500, errors.internal_server_error)
        app.register_error_handler(401, errors.unauthorized)
        app.register_error_handler(405, errors.method_not_allowed)
        app.register_error_handler(409, errors.conflict)

        return app
