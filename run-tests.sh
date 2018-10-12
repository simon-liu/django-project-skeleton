#!/bin/bash

flake8 --max-line-length=200 {{ project_name|lower }}

flake8 --max-line-length=100 apps \
    | grep -v '\/migrations\/.*E501 line too long'

export DJANGO_SETTINGS_MODULE={{ project_name|lower }}.settings.ut

if [ -z "$1" ]
then
    coverage run --source='.' manage.py test \
        apps.main.tests_contract
else
    coverage run --source='.' manage.py test $1
fi
