pipeline {
    agent any

    stages{
        stage('Checkout'){
            steps{
                sh 'echo passed checkout stage'
            }
        }

         stage('Docker Login') {
            steps {
                script {
                    // Use withCredentials to securely access Jenkins stored credentials
                    withCredentials([string(credentialsId: 'docker-hub-password', variable: 'DOCKER_PASSWORD'), 
                                     string(credentialsId: 'docker-hub-username', variable: 'DOCKER_USERNAME')]) {
                        
                        // Execute docker login using the variables provided by withCredentials
                        sh '''
                        echo "Logging into Docker Hub..."
                        docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}
                        '''
                    }
                }
            }
        }
        
        stage('Build and Push Docker Image'){
           steps{
             script{
                sh '''
                echo 'Build Docker Image'
                docker build -t bindu/jenkins-python:latest .
                '''
             }
           }
        }


        stage('Push the artifacts'){
           steps{
             script{
                sh '''
                echo 'Push to docker repo'
                docker push bindu/jenkins-python:latest
                '''
             }
           }
        }

            
        }
    }
