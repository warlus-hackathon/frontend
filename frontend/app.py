from flask import Flask
from frontend.view import index, images


def create_app():
    app = Flask(__name__)

    app.register_blueprint(index.view)
    app.register_blueprint(images.view, url_prefix='/images')

    return app
