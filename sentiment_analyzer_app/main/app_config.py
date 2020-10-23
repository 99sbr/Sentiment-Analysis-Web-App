import os


class Config:
    API_PREFIX = '/api/v1'


class DevelopmentConfig(Config):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    MASTER_CONFIG_FILE = "master.yaml"
    MODEL_IN_USE = "bert_model"
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)