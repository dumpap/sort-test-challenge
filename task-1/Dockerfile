FROM python:3.7-alpine
RUN pip install flask
COPY . /opt/
ENTRYPOINT FLASK_APP=/opt/sortdata.py flask run --host=0.0.0.0 --port=8080