# Sentiment-Analysis-Web-App 🤖 : Built Using Flask-Restplus

- The Flask API structured as follow:
  ![Image](https://github.com/99sbr/Sentiment-Analysis-WebApp/blob/main/Screenshot%202020-10-23%20at%2008.37.54.png)
  
- `manage.py` is the main file to run the application.
- `gunicorn --bind 0.0.0.0:5000 manage:application` command to run the application
- The app is designed for BERT model trained on sentiment analysis data. The is only inference API.
- PRE_TRAINED_MODEL_NAME = 'bert-base-cased'
- Deployed on ec2 instance : `Deep Learning AMI (Ubuntu 18.04) Version 35.0`
