node {
  stage 'Build image'
  dir('app_python'){
    sh "cd app_python && docker build -t lissa00/devops:latest ."
  }
  
  stage 'Push image'
  sh("docker push lissa00/devops:latest")
}
