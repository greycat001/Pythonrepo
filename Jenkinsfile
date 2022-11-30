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
        sh "sudo docker build . -t ${imageName}"
//        script{
//          def dockerImage = docker.build imageName
//        }
      }
    }
    stage('Docker Push') {
      steps {
//        withCredentials([usernamePassword(credentialsId: 'AF_Access', passwordVariable: 'AFPass', usernameVariable: 'AFUser')]) {
        withCredentials([usernamePassword(credentialsId: 'DockehubCredentials', passwordVariable: 'AFPass', usernameVariable: 'AFUser')]) {
          sh 'sudo docker login -u $env.AFUser -p $env.AFPass'
          sh "sudo docker push ${imageName}"
        }
//        script {
//          docker.withRegistry('http://192.168.50.7:8082/artifactory/app1/', 'AF_Access') {
            /* Push the container to the custom Registry */
//            dockerImage.push()
//          }
//        }
      }
    }
  }
} // pipeline
