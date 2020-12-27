prefix=${1}
ASSUME_AWS_ACCOUNT=${2}
if [ "${ASSUME_AWS_ACCOUNT}" == "" ]; then
    ASSUME_AWS_ACCOUNT="636438766403"
fi
echo "ASSUME_AWS_ACCOUNT: ${ASSUME_AWS_ACCOUNT}"
echo "Prefix: ${prefix}"

# export AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}
aws sts get-caller-identity
if [ "${ASSUME_AWS_ACCOUNT}" != "" ]; then
    echo "changing accounts"
    dateTime=$(date +'%Y-%m-%d-%H-%M-%S')
    aws_assumed_role=$(aws sts assume-role --role-arn arn:aws:iam::${ASSUME_AWS_ACCOUNT}:role/BakestackOrgAssumedRole --role-session-name ${dateTime})
    # echo "aws_assumed_role: ${aws_assumed_role}"
    export AWS_ACCESS_KEY_ID=$(echo ${aws_assumed_role}|jq -r '.Credentials.AccessKeyId')
    export AWS_SECRET_ACCESS_KEY=$(echo ${aws_assumed_role}|jq -r '.Credentials.SecretAccessKey')
    export AWS_SECURITY_TOKEN=$(echo ${aws_assumed_role}|jq -r '.Credentials.SessionToken')
fi
aws sts get-caller-identity
aws s3 ls
params="ResourcePrefix=${prefix}"
aws cloudformation deploy \
 --parameter-overrides ${params} \
 --template-file templates/dest_role.yml \
 --stack-name "${prefix}-glaze-role" \
 --capabilities CAPABILITY_NAMED_IAM