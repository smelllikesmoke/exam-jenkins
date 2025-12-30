pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3'
        DEPLOY_DIR = './deploy'
    }
    
    stages {
        stage('Clean') {
            steps {
                echo 'Cleaning workspace...'
                sh '''
                    rm -rf venv/
                    rm -rf ${DEPLOY_DIR}/
                    rm -f test-results.xml
                    echo "Workspace cleaned"
                '''
            }
        }
        
        stage('Checkout') {
            steps {
                echo 'Checking out repository...'
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    python${PYTHON_VERSION} -m venv venv || python3 -m venv venv
                    source venv/bin/activate || . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running pytest tests...'
                sh '''
                    source venv/bin/activate || . venv/bin/activate
                    
                    # Fix: Tell Python to look in the current folder (.) for app.py
                    export PYTHONPATH=.
                    
                    pytest tests/ -v --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }
        
        stage('Build') {
            steps {
                echo 'Building application for deployment...'
                sh '''
                    mkdir -p ${DEPLOY_DIR}
                    cp app.py ${DEPLOY_DIR}/
                    cp requirements.txt ${DEPLOY_DIR}/
                    cp -r tests ${DEPLOY_DIR}/ || true
                    echo "Application built successfully"
                '''
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                    if [ -d "${DEPLOY_DIR}" ]; then
                        echo "Application deployed to ${DEPLOY_DIR}"
                        ls -la ${DEPLOY_DIR}
                    else
                        echo "Deployment directory not found!"
                        exit 1
                    fi
                '''
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}

