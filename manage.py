import os
os.environ['CONFIG'] = 'dev'
from sentiment_analyzer_app import blueprint
from sentiment_analyzer_app.main import create_app

application = create_app(os.environ['CONFIG'])
application.register_blueprint(blueprint)

if __name__ == '__main__':
    application.run()
    # gunicorn --bind 0.0.0.0:5000 manage:application
