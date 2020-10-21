import os
import yaml
from sentiment_analyzer_app.main.app_config import config_by_name
conf = config_by_name[os.environ.get("CONFIG")]

class ConfigurationManager(object):

    def __init__(self, active_directory):
        self.active_directory = active_directory

    def load_conf_from_yaml(self, config_file_name: str):

        with open(os.path.join(conf.BASEDIR, 'utility', 'settings', self.active_directory, config_file_name)) as file:
            config = yaml.safe_load(file)

        return config
