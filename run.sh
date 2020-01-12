#!/bin/bash

virtualenv env
source ./env/bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations Api
python3 manage.py migrate
python3 manage.py data2db
python3 manage.py runserver &
