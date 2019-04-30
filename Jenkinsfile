pipeline {
    agent any 
    stages {
        stage('Build Docker Image') { 
            steps {
                sh 'ls'
                sh 'docker build . -t kudligi/qp'
            }
        }
        stage('Push to Docker Hub') { 
            steps {
                sh 'docker push kudligi/qp'
            }
        }
        stage('Deploy') {
            steps {
                build 'rundeckjob'
            }
        }
        stage('Test'){
            steps{
                sh 'python source/testing.py'
            }
        }
    }
}
