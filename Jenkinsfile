pipeline {
  agent any
  stages {
    stage('Test') {
      steps {
        sh '''
          cd ./app_python
          . .env/bin/activate
          pip install -r requirements.txt
          pip install pytest
          python -m pytest
          deactivate
          '''
      }
    }
  }
}
