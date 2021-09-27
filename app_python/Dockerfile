FROM python:3.6.12-alpine

WORKDIR /app

RUN adduser -D alice

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY app.py .
COPY files/ ./files/
COPY templates/ ./templates/

RUN chmod a+w ./files/file.txt

EXPOSE 8000

USER alice

ENTRYPOINT [ "gunicorn", "-b", "0.0.0.0:8000", "app:app"]
