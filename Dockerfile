# Pull Base Image
FROM python:3.7

# copy code into image and set as working directory
COPY . /application
WORKDIR /application

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python","manage.py"]
