from spacy.lang.en.stop_words import STOP_WORDS
import re


class SentimentAnalyzerService(object):

    def __init__(self, input_text):
        self.input_text = input_text

    def __run_text_preprocessing(self) -> str:
        raw_text_list = self.input_text.split('\n')
        print('removing stopwords')
        raw_text_list = [
            token for token in raw_text_list if token not in STOP_WORDS
        ]
        clean_sent_list = [
            re.sub("[^A-Za-z0-9]./", '', token) for token in raw_text_list
            if bool(token)
        ]
        clean_sent = ' '.join(clean_sent_list)
        clean_sent = ' '.join(clean_sent.split())
        return clean_sent

    def __run_prediction(self) -> str:
        clean_sent = self.__run_text_preprocessing()
        # load model and run predict
        return "Positive"

    def run(self) -> str:
        prediction = self.__run_prediction()
        return prediction

