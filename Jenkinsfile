// pipeline {
//
// agent any
//
// stages {
//
//     stage('Checkout Source Code') {
//         steps {
//             checkout scm
//         }
//     }
//
//     stage('Install Dependencies') {
//         steps {
//             bat '"C:\\Users\\Omveer\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
//             bat '"C:\\Users\\Omveer\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install pytest-html'
//         }
//     }
//
//     stage('Run Tests') {
//         steps {
//             bat '"C:\\Users\\Omveer\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest -vs --html=reports/report.html --self-contained-html'
//         }
//     }
// }
//
// post {
//
//     always {
//
//         archiveArtifacts artifacts: 'reports/**, screenshots/**, logs/**',
//                          allowEmptyArchive: true
//
//         publishHTML([
//             allowMissing: true,
//             alwaysLinkToLastBuild: true,
//             keepAll: true,
//             reportDir: 'reports',
//             reportFiles: 'report.html',
//             reportName: 'Pytest Automation Report'
//         ])
//     }
//
//     success {
//         echo 'Automation Execution Completed Successfully'
//     }
//
//     failure {
//         echo 'Some Test Cases Failed'
//     }
// }
//
// }


pipeline {

    agent any

    stages {

        stage('Checkout Source Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\Omveer\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\Omveer\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest -v'
            }
        }
    }

    post {
        always {
            allure([
                includeProperties: false,
                reportBuildPolicy: 'ALWAYS',
                results: [[path: 'reports/allure-results']]
            ])

            archiveArtifacts artifacts: 'reports/**, screenshots/**',
                             allowEmptyArchive: true
        }

        success {
            echo 'All tests passed!'
        }

        failure {
            echo 'Some tests failed'
        }
    }
}