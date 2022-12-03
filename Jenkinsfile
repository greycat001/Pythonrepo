imageName = 'abcpoi/mypythonapp'

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
    stage('Docker Push') {
      steps {
//        withCredentials([usernamePassword(credentialsId: 'Nexus1Access', passwordVariable: 'RepoPass', usernameVariable: 'RepoUser')]) {

//          sh 'sudo docker login -u $RepoUser -p $RepoPass http://192.168.50.7:8070/repository/myDockerRepo'
//          sh "sudo docker push 192.168.50.7:8070/myDockerRepo/${imageName}"
//        }
//        nexusArtifactUploader artifacts: [[artifactId: 'ArtifactId', classifier: '', file: 'file.gz', type: 'gz']], \
//                              credentialsId: 'Nexus1Access', \
//                              groupId: 'pythonapp', \
//                              nexusUrl: 'http://192.168.50.7:8081', \
//                              nexusVersion: 'nexus3', \
//                              protocol: 'http', \
//                              repository: 'myDockerRepo', \
//                              version: '1.0.0'
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
