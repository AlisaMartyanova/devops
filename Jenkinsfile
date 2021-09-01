pipeline {
  agent {
    docker {
      image 'python:3.6.12-alpine'
    }
  }
  stages {
    stage('Test') {
      steps {
        sh '''
          cd ./app_python
          sh test.sh
          '''
      }
    }
    stage('Build') {
      steps {
        sh 'docker build -t lissa00/devops:latest .'
      }
    }
    stage('Push') {
      steps {
        sh 'docker push lissa00/devops:latest'
      }
    }
  }
}
