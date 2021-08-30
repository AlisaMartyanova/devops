pipeline {
  stages {
    stage('Install dependences') {
      sh "cd ./app_python && pip install -r requirements.txt"
    }

    stage('Test') {
      sh "sh test.sh"
    }
  }
}
