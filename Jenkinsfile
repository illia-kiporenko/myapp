pipeline {
    agent any

    environment {
        APP_NAME = "flask-simple-app"
        IMAGE_NAME = "${APP_NAME}:latest"
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                    cat > Dockerfile <<EOF
                    FROM python:3.10-slim
                    WORKDIR /app
                    COPY . /app
                    RUN pip install --no-cache-dir flask pytest
                    EXPOSE 5000
                    CMD ["python", "app.py"]
                    EOF
                    docker build -t ${IMAGE_NAME} .
                    """
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh """
                    docker run --rm ${IMAGE_NAME} pytest test_app.py > test_output.log || true
                    grep -q 'failed' test_output.log && exit 1 || echo 'All tests passed.'
                    cat test_output.log
                    """
                }
            }
        }

        stage('Run App (Optional)') {
            when {
                expression { return params.RUN_APP == true }
            }
            steps {
                sh "docker run -d -p 5000:5000 --name ${APP_NAME}_container ${IMAGE_NAME}"
            }
        }
    }

    post {
        always {
            echo "Cleaning up..."
            sh "docker rm -f ${APP_NAME}_container || true"
        }
    }

    parameters {
        booleanParam(name: 'RUN_APP', defaultValue: false, description: 'Run the Flask app after testing')
    }
}
