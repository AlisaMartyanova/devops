## TABLE OF CONTENT

 * Application overview
 * Requirements
 * Install and run app
 * Tests
 * Workflow
 
## APPLICATION OVERVIEW
 
This is a simple Python web application (with flask), that shows current time in Moscow. The time is updated with a page refreshing.
By accessing the root page `/` application wites to a `files/file.txt` the following message `"accessed at [time]"`. 
By accessing the `/visits` application reads the content of `files/file.txt` and shows it at this page.

    
## REQUIREMENTS

* Unix OS (to run application from venv)
* Docker (to run application from docker image)
* Free port 8000

## INSTALL AND RUN APP

### Locally from virtualenv

Open command line and run the following commands:

* `git clone https://github.com/AlisaMartyanova/devops.git`
* `cd devops/app_python`
* `sh local_run.sh` - run the application on _localhost:5000_

### Locally with docker (building image manually)

Open command line and run the following commands:

* `git clone https://github.com/AlisaMartyanova/devops.git`
* `cd devops/app_python`
* `docker build -t name[:tag] .` - build docker image with application
* `docker run -d -p 8000:8000 name[:tag]` - run image with application on backgroud on _0.0.0.0:8000_

### Locally from Dockerhub (take ready image)

Open command line and run the following commands:

* `docker run -d -p 8000:8000 lissa00/devops:latest`

## TESTS

Tests are done with _pytest_ library. They are located in the `app_python/test` folder.

To run tests open command line and run the following commands:

* `git clone https://github.com/AlisaMartyanova/devops.git`
* `cd devops/app_python`
* `sh test.sh`

## WORKFLOW STATUS

[![CI to Docker Hub](https://github.com/AlisaMartyanova/devops/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/AlisaMartyanova/devops/actions/workflows/main.yml)
