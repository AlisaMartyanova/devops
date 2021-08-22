## TABLE OF CONTENT

 * Application overview
 * Project structure
 * Requirements
 * Installation
 
## APPLICATION OVERVIEW
 
This is a simple Python web application (with flask), that shows current time in Moscow. The time is updated with a page refreshing.

## PROJECT STRUCTURE


    ├── app_python              # Application folder
    │   ├── .dockerignore        
    │   ├── .gitignore         
    │   ├── DOCKER.md           # Docker best practices
    │   ├── Dockerfile     
    │   ├── PYTHON.md           # Python (web) best practices
    │   ├── app.py              # Application
    │   ├── docker_run.sh       # Run app from docker
    │   ├── local_run.sh        # Run app locally
    │   └── requirements.txt               
    └──
    
## REQUIREMENTS

* Unix OS (to run application locally)
* Docker (to run application from docker image)
* Free port 80

## INSTALLATION

### Locally

* Clone the repository `https://github.com/AlisaMartyanova/devops.git`.
* Cd to the `app_python` folder from command line.
* Run `sh local_run.sh` script from command line.

### From Dockerhub

* Run `docker run -p 80:80 lissa00/devops:time-app` command from command line.


