getLatestVersion() {
    bucketName=${1}
    prefix=${2}
    latest=$(aws s3api list-objects --bucket ${bucketName} --prefix ${prefix} | jq -r '.Contents[].Key' | sed "s#^${prefix}##g" | sed "s#/.*##g" | sort -uV | tail -1)
    if [[ "${latest}" == "" ]]; then
        latest="0.0.0"
    fi
    echo ${latest}
}

getNextVersion() {
    latest=${1}
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
    echo $(python3 ${DIR}/python/get_next_version.py ${latest})
}

# tagRepo() {

# }

# pullDockerImage() {

# }

