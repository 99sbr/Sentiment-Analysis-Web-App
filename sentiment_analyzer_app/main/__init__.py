from flask import Flask
from .app_config import config_by_name
from .model.sentiment_classification.bert_model import load_model
bert_model = load_model()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    return app