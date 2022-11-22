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
        sh "sudo docker build . -t abcpoi/myphythonapp"
      }
    }
  }
} // pipeline
