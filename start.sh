#!/bin/bash
python manage.py makemigrations &&
python manage.py makemigrations ayomi_auth &&
python manage.py migrate &&
python manage.py migrate ayomi_auth &&
python manage.py runserver 0.0.0.0:8000 &&
