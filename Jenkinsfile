pipeline {
    agent any

    tools {
        maven 'Maven'
    }

    stages {

        stage('Git Checkout') {
            steps {
                git 'https://github.com/m-sireesha/basic-programs.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'mvn sonar:sonar'
                }
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t demo-app .'
            }
        }

        stage('Docker Run') {
            steps {
                sh 'docker run -d -p 8081:8080 demo-app'
            }
        }
    }
}



