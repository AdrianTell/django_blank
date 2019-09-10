library identifier: "pipeline-library@v1.1",
retriever: modernSCM(
  [
    $class: "GitSCMSource",
    remote: "https://github.com/redhat-cop/pipeline-library.git"
  ]
)

openshift.withCluster() {

  env.NAMESPACE = openshift.project()
  env.APP_NAME = "APP_NAME"
  env.BUILD = "${env.NAMESPACE}"
  env.DEV = env.BUILD.replace('ci-cd', 'dev')

  env.BUILD_OUTPUT_DIR = env.PIPELINE_CONTEXT_DIR ? "${env.PIPELINE_CONTEXT_DIR}" : "."

  echo "Starting Pipeline for ${APP_NAME}..."

}

pipeline {
  // Use Jenkins Python slave
  agent {
    label 'jenkins-slave-python'
  }

  // Pipeline Stages start here
  stages {

    // Setup Python with PIPENV and create VENV
    stage('Setup Environment') {

        steps {

            sh """
               set -e
               pip install --user pipenv
               cd "${env.BUILD_OUTPUT_DIR}"
               pipenv sync
               pipenv install --dev
               """

        }

    }

    // Run Dependency Check
    stage('Dependency Check') {

        steps {

            sh "pipenv check"

        }

    }

    stage('Build'){
      steps {
        binaryBuild(projectName: env.DEV, buildConfigName: env.APP_NAME, artifactsDirectoryName: "${env.BUILD_OUTPUT_DIR}");
      }
    }

    stage('Promote') {
      steps {
        tagImage(sourceImageName: env.APP_NAME, sourceImagePath: env.DEV, toImagePath: env.DEV)
      }
    }

    //stage ('Verify Deployment to Dev') {
    //  steps {
    //    verifyDeployment(projectName: env.DEV, targetApp: env.APP_NAME)
    //  }
    //}
  }
}
