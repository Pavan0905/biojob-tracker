pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker compose build'
            }
        }

        stage('Start App') {
            steps {
                echo 'Starting the application...'
                sh 'docker compose up -d'
            }
        }

        stage('Check App') {
            steps {
                echo 'Checking app status...'
                sh 'curl -I http://localhost:8000 || true'
            }
        }
    }
}
