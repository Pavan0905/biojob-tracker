pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Start App') {
            steps {
                sh 'docker compose up -d'
            }
        }

        stage('Check App') {
            steps {
                sh 'curl --fail http://localhost:8000 || exit 1'
            }
        }
    }
}
