import os
from sentiment_analyzer_app.main.app_config import config_by_name
from sentiment_analyzer_app.main.model.sentiment_classification.bert_model import bert

conf = config_by_name[os.environ['CONFIG']]


class SentimentAnalyzerService(object):

    def __init__(self, input_text):
        self.input_text = input_text

    def __run_prediction(self) -> str:
        model = bert.Prediction()
        sentiment = model.predict(self.input_text)
        # load model and run predict
        return sentiment

    def run(self) -> str:
        print('Running Prediction')
        prediction = self.__run_prediction()
        return prediction
