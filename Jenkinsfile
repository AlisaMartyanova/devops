pipeline {
  agent {
    docker { image 'python:3.6.12-alpine'}
  }
  stages {
    stage('Install dependences') {
      steps {
        sh "cd ./app_python && pip install -r requirements.txt"
      }
    }

    stage('Test') {
      steps {
        sh "sh test.sh"
      }
    }
  }
}
