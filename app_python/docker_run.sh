export FLASK_APP=app.py
gunicorn -b 0.0.0.0:80 app:app
