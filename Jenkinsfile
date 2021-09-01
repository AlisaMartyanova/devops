pipeline {
  agent none
  stages {
    stage('Test') {
      agent {
        docker {
          image 'python:2-alpine'
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
