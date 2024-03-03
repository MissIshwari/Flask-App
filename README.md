# Flask-App
Flask app that deployment with jenkins and github actions.

The Jenkinsfile in this repository is a declarative jenkins file.
Environment variables are declared for github repository, branch to run the pipeline on, SSH_USER and SSH_EC2 instance for deployment.

There are exactly 4 stages in my pipeline, namely
Cloning the flask application, building the application, testing it and deploying to a staging area.

Selected Poll SCM option in jenkins pipeline to trigger with a per minute schedule.


Github action -
main.yml within .github/workflows folder executes whenever there is a new commit in staging branch, 
Created github secrets for deployment.

