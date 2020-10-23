import os

import torch
from torch import nn
from transformers import BertModel, BertTokenizer

from sentiment_analyzer_app.main import bert_model
from sentiment_analyzer_app.main.app_config import config_by_name
from sentiment_analyzer_app.main.model.sentiment_classification.prediction_interface_class import AbstractPrediction
from sentiment_analyzer_app.main.utility.manager.configuration import ConfigurationManager

conf = config_by_name[os.environ.get("CONFIG")]
PRE_TRAINED_MODEL_NAME = ConfigurationManager(conf.MODEL_IN_USE).load_conf_from_yaml("model_config.yaml")[
    'PRE_TRAINED_MODEL_NAME']
tokenizer = BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)


class SentimentClassifier(nn.Module):

    def __init__(self, n_classes):
        super(SentimentClassifier, self).__init__()
        self.bert = BertModel.from_pretrained(PRE_TRAINED_MODEL_NAME)
        self.drop = nn.Dropout(p=0.3)
        self.out = nn.Linear(self.bert.config.hidden_size, n_classes)

    def forward(self, input_ids, attention_mask):
        _, pooled_output = self.bert(
            input_ids=input_ids,
            attention_mask=attention_mask
        )
        output = self.drop(pooled_output)

        return self.out(output)


class Prediction(AbstractPrediction):

    def __init__(self):
        super(Prediction, self).__init__()

    @staticmethod
    def __preprocess_input(input_text: str) -> str:
        import re
        preprocessed_text = re.sub(r'[^A-Za-z0-9]+', ' ', input_text)
        return preprocessed_text

    def predict(self, input_text: str) -> str:
        print('Preprocessing')
        sentiment_map = {'negative': 0, 'neutral': 1, 'positive': 2}
        class_names = sentiment_map.keys()
        preprocessed_text = Prediction.__preprocess_input(input_text)
        encoded_review = tokenizer.encode_plus(
            preprocessed_text,
            max_length=60,
            add_special_tokens=True,
            return_token_type_ids=False,
            pad_to_max_length=True,
            return_attention_mask=True,
            return_tensors='pt',
        )
        input_ids = encoded_review['input_ids'].to('cpu')
        attention_mask = encoded_review['attention_mask'].to('cpu')
        print('Running Prediction')
        output = bert_model(input_ids, attention_mask)

        _, prediction = torch.max(output, dim=1)

        print(f'Review text: {preprocessed_text}')
        print(f'Sentiment  : {list(class_names)[prediction.tolist()[0]]}')
        sentiment = list(class_names)[prediction.tolist()[0]]
        return sentiment
