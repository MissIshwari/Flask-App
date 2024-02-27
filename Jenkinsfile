pipeline{
  agent any
  environment{
        GITHUB_URL='https://github.com/MissIshwari/Flask-App.git'
        BRANCH='main'
        SSH_USER='ubuntu'
        SSH_EC2='3.235.86.233'
    }
  stages{
    stage('Clone github'){
            steps{
                git branch: env.BRANCH, url: env.GITHUB_URL
            }
    }
    stage('Copying to EC2'){
            steps{
                sshagent(credentials: ['ishwari']) {
                    script {
                        sh """
                            ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SSH_EC2} '
                                cd /var/www/html/;
                                ls
                                
                                
                            '
                        
                        
                            scp -o StrictHostKeyChecking=no -r * ${SSH_USER}@${SSH_EC2}:/home/ubuntu
                        """
                    }
            }
            }
            
        }
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
    stage("Test"){
      steps{
        sshagent(credentials:['credentials']){
          sh '''
          pytest hello_test.py
          '''
        }
      }
    }
    stage("Deployment to staging"){
      steps{
        sshagent(credentials:['credentials']){
          sh '''
          
          '''
        }
      }
    }
  }
}
