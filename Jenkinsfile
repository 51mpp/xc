pipeline{
    agent any

    environment {
        IMAGE_NAME = "https://hub.docker.com/repository/docker/51mpp/test1/general"
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
            agent{
                label 'vm2-tester'
            }
            steps{
                    // push the image to the gitlab registry with credentials
                    withCredentials([usernamePassword(credentialsId: 'decf1751-1114-490d-8ad0-3488025ffa77', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh 'docker login -u ${USERNAME} -p ${PASSWORD} registry.gitlab.com'
                        sh 'docker push docker push 51mpp/test1'
                    }
                    sh 'docker rmi -f docker push 51mpp/test1'
                    // sh "docker push https://hub.docker.com/repository/docker/51mpp/test1/general"
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
                    withCredentials([usernamePassword(credentialsId: '86130d73-f735-4fd7-b9c7-6922adffce72', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                        sh 'docker login -u ${USERNAME} -p ${PASSWORD} registry.gitlab.com'
                        sh 'docker pull https://hub.docker.com/repository/docker/51mpp/test1/general'
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