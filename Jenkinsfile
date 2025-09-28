pipeline {
    agent any

    stages{
        stage('Checkout'){
            steps{
                sh 'echo passed checkout stage'
            }
        }

        
        stage('Build and Push Docker Image'){
           steps{
             script{
                sh '''
                echo 'Build Docker Image'
                docker build -t bindu/jenkins-python
                '''
             }
           }
        }


        stage('Push the artifacts'){
           steps{
             script{
                sh '''
                echo 'Push to docker repo'
                docker push -t bindu/jenkins-python
                '''
             }
           }
        }

            
        }
    }
