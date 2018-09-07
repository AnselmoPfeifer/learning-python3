def branch = env.GIT_BRANCH

def gitHubCheckout(branch) {
    checkout([$class: 'GitSCM',
              branches: [[name: branch]],
              browser: [$class: 'GithubWeb', repoUrl: 'https://github.com/AnselmoPfeifer/learning-python3.git'],
              userRemoteConfigs: [[credentialsId: 'git-anspfeifer',
                                   url: 'https://github.com/AnselmoPfeifer/learning-python3.git']
              ]])
}

node() {

    stage('Git Checkout') {
        gitHubCheckout(branch)
    }

    stage('SonarQube-Scan') {
        def scannerHome = tool 'SymphonySonarScanner'
        script{
            sh('bash dependencies.sh > env.txt')
            sh("${scannerHome}/bin/sonar-scanner -Dsonar.host.url=${SONAR_URL}")
        }

        archiveArtifacts(artifacts: 'env.txt', allowEmptyArchive: true)
    }
}