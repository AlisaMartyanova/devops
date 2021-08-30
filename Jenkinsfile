node {
  stage 'Build image'
  dir('app_python'){
    sh "docker build -t lissa00/devops:latest ."
  }
  
  stage 'Push image'
  sh("docker push lissa00/devops:latest")
}
