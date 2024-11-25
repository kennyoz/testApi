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
                    // Установка Python и pip (если не установлены)
                    sh 'which python3 || (sudo apt update && sudo apt install -y python3 python3-pip)'

                    // Установка Python зависимостей
                    sh 'pip3 install -r requirements.txt'

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
                    sh 'pytest --alluredir=allure-results test_api.py'
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
