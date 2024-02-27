pipeline{
  agent any
  environment{
        GITHUB_URL='https://github.com/MissIshwari/Flask-App.git'
        BRANCH='main'
        SSH_USER='ubuntu'
        SSH_EC2='3.235.16.31'
    }
  stages{
    stage('Clone github repo flask project'){
            steps{
                git branch: env.BRANCH, url: env.GITHUB_URL
            }
    }
    stage("Build"){
      steps{
        
          sh '''
          sudo apt update
          sudo apt install python
          sudo pip install -r requirements.txt
          
          '''
        
      }
    }
    stage("Test"){
      steps{
        sshagent(credentials:['credentials']){
          sh '''
          flask run
          pytest ./tests/hello_test.py
          '''
        }
      }
    }
    stage('Deploying to EC2'){
            steps{
                sshagent(credentials: ['ishwari']) {
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
