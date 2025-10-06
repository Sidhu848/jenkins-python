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
        
        stage('Build Docker Image'){
           steps{
             script{
                sh '''
                echo 'Build Docker Image'
                docker build -t bindu039/jenkins-python:latest .
                '''
             }
           }
        }


        stage('Push the docker image'){
           steps{
             script{
                sh '''
                echo 'Push to docker repo'
                docker push bindu039/jenkins-python:latest
                '''
             }
           }
        } 

        stage("update deployment file"){
            environment {
                GIT_REPO_NAME = "jenkins-python"
                GIT_USER_NAME = "Sidhu848"
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'github', usernameVariable: 'GIT_USERNAME', passwordVariable: 'GIT_TOKEN')]) {                sh """
                 git config user.email "sudarshan.sudeer@gmail.com"
                 git config user.name "Sidhu848"
                 BUILD_NUMBER=${BUILD_NUMBER}
                 sed -i "s/replaceImageTag/${BUILD_NUMBER}/g" deploy/deployment.yml
                 git add deploy/deployment.yml
                 git commit -m "Update deployment image to version ${BUILD_NUMBER}"
                 git push https://${GITHUB_TOKEN}@github.com/${GIT_USER_NAME}/${GIT_REPO_NAME} HEAD:main
                """
                }
            }
        }
     }
 }
