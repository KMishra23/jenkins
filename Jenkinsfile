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
                bat "chmod u+x armstrong.py"
                bat "./armstrong.py"
            }
        }
        stage('Test Set 1(Pass)') {
            steps {
                bat "chmod u+x unitTest1.py"
                bat "./unitTest1.py"
            }
        }
        stage('Test Set 2(Fail)') {
            steps {
                bat "chmod u+x unitTest2.py"
                bat "./unitTest2.py"
            }
        }
    } 
}
