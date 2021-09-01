pipeline {
  agent any
  stages {
    stage('Test') {
      agent {
        docker {
          image 'python:3.6.12-alpine'
        }
      }
      steps {
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
