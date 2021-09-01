pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        withPythonEnv('python3') {
          sh '''
            cd ./app_python
            pip install -r requirements.txt
            pip install pytest
            python -m pytest
            '''
        }
      }
    }
  }
}
