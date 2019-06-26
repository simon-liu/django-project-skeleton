#!/bin/bash

flake8 --max-line-length=200 {{ project_name|lower }} \
    --ignore W391 \
    --per-file-ignores '{{ project_name|lower }}/settings/*.py:F405,F403,F401'

flake8 --max-line-length=100 apps \
    --ignore W391 \
    --exclude apps/*/migrations/*.py

export DJANGO_SETTINGS_MODULE={{ project_name|lower }}.settings.ut

if [[ -z "$1" ]]
then
    coverage run --source='.' manage.py test \
        apps.main.tests_main
else
    coverage run --source='.' manage.py test $1
fi
