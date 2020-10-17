from flask_restplus import Namespace, fields


class SentimentAnalyzer:
    api = Namespace('Sentiment Analysis', description='Perform Sentiment Analysis on Text')
    payload = api.model('SentimentAnalyzer',
                        {
                            'InputText': fields.String(required=True, description='Input Text to be analyzed')
                        })
