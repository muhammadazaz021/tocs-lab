pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/muhammadazaz021/tocs lab.git'
            }
        }
        stage('Execute Script') {
            steps {
                sh 'python fib.py'
            }
        }
    }
}
