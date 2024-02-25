pipeline{
  agent any
  stages{
    stage("Build"){
      steps{
        sshagent(credentials : ['credentials']){
          sh '''
          sudo apt update
          sudo apt install python
          sudo pip install -r requirements.txt
          
          '''
        }
      }
    }
  }
}
