#!/bin/bash

flake8 --max-line-length=200 {{ project_name|lower }}

flake8 --max-line-length=100 apps --exclude apps/*/migrations/*.py

export DJANGO_SETTINGS_MODULE={{ project_name|lower }}.settings.ut

if [[ -z "$1" ]]
then
    coverage run --source='.' manage.py test \
        apps.main.tests_main
else
    coverage run --source='.' manage.py test $1
fi
