from abc import ABC


class AbstractPrediction(ABC):

    def __init__(self):
        super().__init__()

    def preprocess_input(self, input_text):
        raise NotImplementedError()

    def load_model(self):
        raise NotImplementedError()

    def predict(self, input_text):
        raise NotImplementedError()
