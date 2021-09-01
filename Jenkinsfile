pipeline {
  agent any
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
