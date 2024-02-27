pipeline{
  agent any
  environment{
        GITHUB_URL='https://github.com/MissIshwari/Flask-App.git'
        BRANCH='main'
        SSH_USER='ubuntu'
        SSH_EC2='13.41.186.190'
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
                            ssh -o StrictHostKeyChecking=no ${SSH_USER}@${SSH_EC2} '
                                sudo apt update
                                sudo apt install python
                                sudo apt install pip
                                sudo python -m pip install -r requirements.txt
                            '
                            scp -o StrictHostKeyChecking=no -r * ${SSH_USER}@${SSH_EC2}:/home/ubuntu
                            flask run
                        """
                    }
            }
        }
        
      }
    }
    stage("Test"){
      steps{
        sshagent(credentials:['ishwari-california-vired']){
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
