## TABLE OF CONTENT

 * Application overview
 * Project structure
 * Requirements
 * Install and run app
 
## APPLICATION OVERVIEW
 
This is a simple Python web application (with flask), that shows current time in Moscow. The time is updated with a page refreshing.

## PROJECT STRUCTURE


    ├── app_python              # Application folder
    │   ├── templates           # Html templates
    │   │   └── ...
    │   ├── .dockerignore              
    │   ├── DOCKER.md           # Docker best practices
    │   ├── Dockerfile     
    │   ├── PYTHON.md           # Python (web) best practices
    │   ├── app.py              # Application
    │   ├── local_run.sh        # Run app locally
    │   └── requirements.txt    # Python packages required to the project.    
    ├── .gitignore   
    └── README.md
    
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

* `docker run -d -p 8000:8000 lissa00/devops:latest
