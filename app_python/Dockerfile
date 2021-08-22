FROM python:3.6.12-alpine

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt && \
    pip3 install gunicorn

COPY . /app

ENTRYPOINT [ "sh" ]

CMD [ "docker_run.sh" ]
