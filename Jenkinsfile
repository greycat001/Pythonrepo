pipeline {
  agent any
  stages {
    stage('Checkout') {
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
