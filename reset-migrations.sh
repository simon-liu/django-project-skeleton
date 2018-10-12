#!/bin/bash

mv apps/main/migrations/*.py /tmp/
cp /tmp/__init__.py apps/main/migrations/
python3 manage.py makemigrations