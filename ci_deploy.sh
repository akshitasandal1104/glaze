export AWS_ACCESS_KEY_ID=${CI_AWS_ACCESS_KEY_ID}
export AWS_SECRET_ACCESS_KEY=${CI_AWS_SECRET_ACCESS_KEY}
export AWS_DEFAULT_REGION=${CI_AWS_DEFAULT_REGION}
source shared_libraries/artifacts.sh
filename="glaze-deploy"
bucketName="glaze-ami-builder-deploy-${AWS_ACCOUNT}-${AWS_DEFAULT_REGION}"
tar -cvf ${filename}.tar.gz .
prefix="artifacts/branch/${CI_COMMIT_BRANCH}/glaze/"
latest=$(getLatestVersion ${bucketName} ${prefix})
next_version=$(getNextVersion ${latest})
aws s3api put-object --bucket ${bucketName} --key ${prefix}${next_version}/${filename}.tar.gz --body ${filename}.tar.gz
