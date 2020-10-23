from flask import Blueprint
from flask_restplus import Api
from sentiment_analyzer_app.main.controller.sentiment_analyzer_controller import api as ns_sentiment_analyzer

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Sentiment Analysis API',
          version='1.0',
          description='Flask restplus web service for Sentiment Analysis App'
          )

api.add_namespace(ns_sentiment_analyzer)
