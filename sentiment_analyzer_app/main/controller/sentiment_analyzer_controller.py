from flask_restplus import Resource

from sentiment_analyzer_app.main.services.sentiment_analyzer_service import SentimentAnalyzerService
from sentiment_analyzer_app.main.utility.payloads.sentiment_analyzer_payload import SentimentAnalyzer

api = SentimentAnalyzer.api
payload = SentimentAnalyzer.payload


@api.route("/get-sentiment")
@api.response(200, "Success")
@api.response(400, "Bad Response")
@api.response(404, "Not Found")
@api.response(500, "Internal Server error")
class SentimentAnalysis(Resource):
    """
    Run Sentiment Analysis model on Input Text
    """

    @api.doc("Get Sentiment")
    @api.expect(payload, validate=True)
    def post(self):
        # noinspection PyBroadException
        try:
            input_text = self.api.payload['InputText']
            sentiment = SentimentAnalyzerService(input_text=input_text).run()

            return {'Response': sentiment}
        except Exception as e:
            self.api.abort(500)
