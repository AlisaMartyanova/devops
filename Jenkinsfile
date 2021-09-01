pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        withPythonEnv('python3') {
          sh '''
            cd ./app_python
            sh test.sh
            '''
        }
      }
    }
  }
}
