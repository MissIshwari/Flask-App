pipeline{
  agent any
  environment{
        GITHUB_URL='https://github.com/MissIshwari/Flask-App.git'
        BRANCH='main'
        SSH_USER='ubuntu'
        SSH_EC2='18.130.98.247'
    }
  stages{
    stage('Clone github repo flask project'){
            steps{
                git branch: env.BRANCH, url: env.GITHUB_URL
            }
    }
    stage("Build"){
      steps{
        script{
          sshagent(credentials: ['ishwari-california-vired']) {
                    script {
                        sh """
                            scp -o StrictHostKeyChecking=no -r * ${SSH_USER}@${SSH_EC2}:/home/ubuntu
                            
                            ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SSH_EC2} '
                                sudo apt update
                                sudo apt install python3
                                sudo apt install pip -y
                                sudo pwd
                                sudo pip install -r requirements.txt
                            '
                            
                        """
                    }
            }
        }
        
      }
    }
    stage("Test"){
      steps{
        sshagent(credentials: ['ishwari-california-vired']){
          sh '''
          flask run
          pytest ./tests/hello_test.py
          '''
        }
      }
    }
    stage('Deploying to EC2'){
            steps{
                sshagent(credentials: ['ishwari-california-vired']) {
                    script {
                        sh """
                            ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SSH_EC2} '
                                cd /var/www/html/;
                                ls
                            '
                            scp -o StrictHostKeyChecking=no -r * ${SSH_USER}@${SSH_EC2}:/home/ubuntu
                            flask run
                        """
                    }
            }
            }
            
        }
  }
}
