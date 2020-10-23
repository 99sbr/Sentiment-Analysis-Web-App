import os

import torch
from torch import nn
from transformers import BertModel

from sentiment_analyzer_app.main.app_config import config_by_name
from sentiment_analyzer_app.main.utility.manager.configuration import ConfigurationManager

conf = config_by_name[os.environ.get("CONFIG")]
PRE_TRAINED_MODEL_NAME = ConfigurationManager(conf.MODEL_IN_USE).load_conf_from_yaml("model_config.yaml")[
    'PRE_TRAINED_MODEL_NAME']

checkpoint = torch.load(ConfigurationManager('bert_model').load_conf_from_yaml('model_config.yaml')[
                            'best_model_path'], map_location=torch.device('cpu'))


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


def load_model():
    sentiment_map = {'negative': 0, 'neutral': 1, 'positive': 2}
    class_names = sentiment_map.keys()
    model = SentimentClassifier(len(class_names))
    model.load_state_dict(checkpoint)
    model.to('cpu')
    for param in model.parameters():
        param.requires_grad = False

    return model
