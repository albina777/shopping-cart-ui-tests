pipeline {
    agent any

    environment {
        VENV_DIR = ".venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Python & Dependencies') {
            steps {
                sh '''
                    set -e
                    python3 -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Install Browsers') {
            steps {
                sh '''
                    set -e
                    source ${VENV_DIR}/bin/activate
                    playwright install chromium firefox webkit
                '''
            }
        }

        stage('Run Tests with Allure') {
            steps {
                sh '''
                    set -e
                    source ${VENV_DIR}/bin/activate
                    pytest --alluredir=allure-results --junitxml=allure-results/results.xml
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                    set -e
                    allure generate allure-results --clean -o allure-report
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', reportBuildPolicy: 'ALWAYS', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'screenshots/*.png', fingerprint: true
            junit 'allure-results/results.xml'
        }
    }
}
