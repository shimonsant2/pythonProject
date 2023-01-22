pipeline {
    agent any
    stages {
        stage('Installing packages') {
            steps {
                script {
                    sh 'pwd'
                    sh 'ls -l'
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('Static Code Checking') {
            steps {
                script {
                    sh 'find . -name \\*.py | xargs pylint -f parseable | tee pylint.log'
                    recordIssues(
                        tool: pyLint(pattern: 'pylint.log'),
                        unstableTotalHigh: 100,
                    )
                }
            }
        }
        stage ('for the fix branch') {
          when {
            branch "fix-*"
          }
          steps {
            sh echo 'this only run for the fixes'
           }
        }
        stage ('for the fix branch') {
          when {
            branch "PR-*"
          }
          steps {
            sh echo 'this only run for the PRs'
           }
        }
        stage('Running Unit tests') {
            steps {
                script {
                    sh 'python3 -m pytest --junitxml=pyunit.xml --cov=. --cov-report xml'
                    step([$class: 'CoberturaPublisher',
                        coberturaReportFile: "coverage.xml",
                        onlyStable: false,
                        failNoReports: true,
                        failUnhealthy: false,
                        failUnstable: false,
                        autoUpdateHealth: true,
                        autoUpdateStability: true,
                        zoomCoverageChart: true,
                        maxNumberOfBuilds: 10,
                        lineCoverageTargets: '80, 80, 80',
                        conditionalCoverageTargets: '80, 80, 80',
                        classCoverageTargets: '80, 80, 80',
                        fileCoverageTargets: '80, 80, 80',
                    ])
                    junit "pyunit.xml"
                }
            }
        }
    }
}