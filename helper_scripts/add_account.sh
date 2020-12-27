#!/bin/bash
ACCOUNT=${1}
URL=${2}
echo "ACCOUNT ${ACCOUNT}"
echo "URL ${URL}"
curl -X POST ${URL} \
-H "Accept: application/json" \
-d "{\"account\": \"${ACCOUNT}\"}"
