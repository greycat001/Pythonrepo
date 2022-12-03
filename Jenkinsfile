imageName = 'abcpoi/mypythonapp'
def dockerImage

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
        script{
          dockerImage = docker.build imageName
        }
      }
    }
    stage('Docker Push') {
      steps {
        script {
          docker.withRegistry('http://192.168.50.7:8070/myDockerRepo', 'Nexus1Access') {
            /* Push the container to the custom Registry */
            dockerImage.push()
          }
        }
      }
    }
  }
} // pipeline
