import os
from flask import Flask
from flask_bootstrap import Bootstrap

from server.config.config import DevelopmentConfig


def create_app(script_info=None):

    # instantiate the app
    app = Flask(
        __name__,
        #template_folder="../client/templates",
        #static_folder="../client/public",
    )

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    if(app_settings is None):
        app_settings = DevelopmentConfig

    app.config.from_object(app_settings)

    # set up extensions
    Bootstrap(app)

    # register blueprints
    from .controllers import main_controller

    app.register_blueprint(main_controller.main_controller)

    # shell context for flask cli
    app.shell_context_processor({"app": app})

    return app
