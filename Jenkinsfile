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
          virtualenv venv --distribute
          . venv/bin/activate 
          pip install -r requirements.txt
          sh test.sh
          '''
      }
    }
  }
}
