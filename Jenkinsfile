pipeline {
  agent any

  stages {
    stage(' Build Docker Image') {
      steps {
        echo 'Building Docker image...'
        sh 'docker compose build'
      }
    }

    stage(' Start App') {
      steps {
        echo 'Running Docker container...'
        sh 'docker compose up -d'
      }
    }

    stage(' Check App') {
      steps {
        echo 'Checking app availability...'
        sh 'curl -I http://localhost:8000 || true'
      }
    }
  }
}
