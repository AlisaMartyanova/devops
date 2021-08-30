pipeline {
  agent any
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
