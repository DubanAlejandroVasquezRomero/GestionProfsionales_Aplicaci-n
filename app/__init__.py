from flask import Flask
import os

def create_app ():

    app = Flask (__name__)

    app.config.from_mapping (
        SECRET_KEY = 'mikey',
        DATABASE= os.environ.get ('FLASK_DATABASE'),
        DATABASE_HOST = os.environ.get ('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD = os.environ.get ('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER = os.environ.get ('FLASK_DATABASE_USER'),
    )

    from . import db,auth,routes,admin

    db.init_app (app)
    app.register_blueprint (auth.bp)
    app.register_blueprint (routes.bp)
    app.register_blueprint (admin.bp)

    return app

