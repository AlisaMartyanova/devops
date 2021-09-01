pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh '''
          cd ./app_python
          sh test.sh
          '''
      }
    }
  }
}
