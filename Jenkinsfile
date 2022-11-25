pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/KMishra23/jenkins.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x armstrong.py"
                sh "./armstrong.py"
            }
        }
        stage('Test Set 1(Pass)') {
            steps {
                sh "chmod u+x unitTest1.py"
                sh "./unitTest1.py"
            }
        }
        stage('Test Set 2(Fail)') {
            steps {
                sh "chmod u+x unitTest2.py"
                sh "./unitTest2.py"
            }
        }
    } 
}
