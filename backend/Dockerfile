FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /backend
COPY . /backend

RUN pip install -r requirements.txt --no-cache-dir && \
    sed -i -e 's/{% load staticfiles %}/{% load static %}/' /usr/local/lib/python3.7/site-packages/rest_framework_swagger/templates/rest_framework_swagger/index.html

COPY ./openapi.py /usr/local/lib/python3.7/site-packages/rest_framework/schemas

CMD ["gunicorn", "--env", "DJANGO_SETTINGS_MODULE=app.settings.production", "app.wsgi", "-b", "0.0.0.0:$PORT", "-t", "300", "--threads", "10", "--workers", "10", "--max-requests", "1000", "--max-requests-jitter", "50"]
