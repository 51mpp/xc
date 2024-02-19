pipeline{
    agent any

    environment {
        IMAGE_NAME = "https://hub.docker.com/repository/docker/51mpp/test1/general"
        DOCKER_CREDENTIALS = credentials('095a317d-a951-411f-8be6-6dce905b9986')
    }

    stages{
        stage("Set Enviroment") {
            agent {
                label 'vm2-tester'
            }
            steps {
                
                sh 'python3 -m venv myenv'
            }
        }
        stage("Install lib") {
            agent {
                label 'vm2-tester'
            }
            steps {
                sh '''#!/bin/bash
                source myenv/bin/activate && pip install -r ./requirements.txt
                
                '''
            }
        }
        stage("Run Unit Test") {
            agent{
                label 'vm2-tester'
            }
            steps {
                sh '''#!/bin/bash
                source myenv/bin/activate && python3 ./test_restapi.py
                '''
            }
        }
        stage("Create Images") {
            agent {
                label 'vm2-tester'
            }
            steps {
                sh "docker compose build"
                sh "docker ps"
            }
        }
        stage("Create Container") {
            agent{
                label 'vm2-tester'
            }
            steps {
                sh "docker compose up -d"
            }
        }
        stage("Clone Robot") {
            agent{
                label 'vm2-tester'
            }
            steps {
                sh "rm -rf RobotTestScript"
                withCredentials([gitUsernamePassword(credentialsId: '86130d73-f735-4fd7-b9c7-6922adffce72', gitToolName: 'git-tool')]) {
                    // Use withCredentials block to securely access credentials
                    sh 'git clone https://github.com/SDPP-Group/RobotTestScript.git'
                }
            }
        }
        stage("Run Robot Test") {
            agent{
                label 'vm2-tester'
            }
            steps {
                // sh "cd ./robottestapi && robot ./plus.robot"
                sh "cd ./RobotTestScript && python3 -m robot ./plus.robot"
                
            }
        }
        stage("Push Image") {
            agent {
                label 'vm2-tester'
            }
            steps {
                // Push the image to the Docker Hub registry with credentials
                withCredentials([usernamePassword(credentialsId: '095a317d-a951-411f-8be6-6dce905b9986', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh "echo $PASSWORD docker login -u $USERNAME --password-stdin"
                    sh "docker tag 51mpp/test1:latest 51mpp/test1:latest"
                    sh "docker push 51mpp/test1:latest"
                }
                // Remove the local image after pushing it to the registry
                sh "docker rmi -f 51mpp/test1:latest"
            }
        }
        stage('Clean Workspace') {
            agent {
                label 'vm2-tester'
            }
            steps {
                sh 'docker compose -f ./compose.yml down'          
                sh 'docker system prune -a -f'
            }
        }
        stage('Pull Image from Registry') {
            agent {
                label 'vm3-pre-prod'
            }
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'd2aa59b5-0231-43f0-98ef-a74ff32918ba', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh "echo $PASSWORD | docker login -u $USERNAME --password-stdin"
                        sh 'docker pull 51mpp/test1'
                    }
                }
            }
        }
        stage('Create Container from Image') {
            agent {
                label 'vm3-pre-prod'
            }
            steps {
                sh "docker compose -f ./compose.yml up -d"
            }
        }
    }
    
}