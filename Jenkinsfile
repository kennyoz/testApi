pipeline {
    agent any

    environment {
        ALLURE_HOME = "${WORKSPACE}/allure-2.13.5"
        PATH = "${ALLURE_HOME}/bin:${env.PATH}"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Установка Python зависимостей
                    sh 'pip install -r requirements.txt'

                    // Установка Allure Commandline
                    sh 'wget https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.5/allure-commandline-2.13.5.tgz'
                    sh 'tar -zxvf allure-commandline-2.13.5.tgz'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Запуск тестов с использованием pytest и сохранение результатов в allure-results
                    sh 'pytest --alluredir=allure-results'
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                script {
                    // Генерация Allure отчета
                    sh 'allure generate allure-results -o allure-report --clean'
                }
            }
            post {
                always {
                    // Архивирование Allure отчета
                    archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
                }
            }
        }
    }

    post {
        always {
            // Очистка рабочей директории
            cleanWs()
        }
    }
}