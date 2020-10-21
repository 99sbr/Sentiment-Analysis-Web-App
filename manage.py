import os
os.environ['CONFIG'] = 'dev'
from werkzeug.utils import cached_property
from sentiment_analyzer_app import blueprint
from sentiment_analyzer_app.main import create_app
from flask_script import Manager
from waitress import serve

app = create_app('test')
app.register_blueprint(blueprint)
manager = Manager(app)


@manager.command
def run():
    serve(app, port=1234)


if __name__ == '__main__':
    manager.run()
