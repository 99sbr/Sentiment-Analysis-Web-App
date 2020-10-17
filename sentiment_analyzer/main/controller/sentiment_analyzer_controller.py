from flask_restplus import Resource
from sentiment_analyzer.main.utility.payloads.sentiment_analyzer_payload import SentimentAnalyzer

api = SentimentAnalyzer.api
payload = SentimentAnalyzer.payload

@api.route("/get-sentiment")
@api.response(200, "Success")
@api.response(400, "Bad Response")
@api.response(404, "Not Found")
@api.response(500, "Internal Server error")
class AddressSearch(Resource):
    """
    Performs Address Search on Web Data for Client Profile
    """

    @api.doc("Get Sentiment")
    @api.expect(payload, validate=True)
    def post(self):
        # noinspection PyBroadException
        try:
            input_text = self.api.payload['InputText']
            sentiment = main_call()
            return {'Response': sentiment}
        except Exception as e:
            self.api.abort(500)