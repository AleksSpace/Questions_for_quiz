#!/bin/bash
python manage.py migrate --noinput && \
python manage.py collectstatic --no-input && \
gunicorn quiz.wsgi:application --bind 0:8000