from flask import Flask, redirect, url_for
from . import config
from database import db
from report import report


def register_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    app.register_blueprint(report, url_prefix='/report')


def create_app(config=config.base_config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    register_blueprints(app)

    return app


app = create_app()


@app.route('/')
def default():
    return redirect(url_for('report.list'))
