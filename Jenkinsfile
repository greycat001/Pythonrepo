imageName = 'abcpoi/myphythonapp'

pipeline {
  agent any
  options {
    skipDefaultCheckout(true)
  }
  stages {
    stage('Checkout') {
      steps {
        cleanWs()
        checkout scm
      }
    }
    stage('Build') {
      steps {
//        sh "sudo docker build . -t ${imageName}"
        script{
          def dockerImage = docker.build imageName
        }
      }
    }
  }
} // pipeline
