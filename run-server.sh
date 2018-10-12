#!/bin/bash

export DJANGO_SETTINGS_MODULE={{ project_name|lower }}.settings.local

python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver
