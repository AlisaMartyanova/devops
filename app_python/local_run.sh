#!/bin/bash

python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=app.py
gunicorn -b 127.0.0.1:5000 app:app
