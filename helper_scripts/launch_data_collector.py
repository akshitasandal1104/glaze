import sys
import json
import base64
import boto3


def get_lambda_client():
    return boto3.client("lambda")

def handler(args):
    account_id = "325960980908"
    resource_prefix = args[1]
    if len(args) == 3:
        account_id = args[2]


    event = {"environmentVariables": [
            {   
                "name": "CONFIG_URL",
                "value": f"http://{resource_prefix}-glaze.bakestack.com/api/config/batch,inventory/prd/latest"
            },
            {
                "name": "CONFIG_CREDENTIALS",
                "value": "dXNlcjpwYWNtYW4="
            },
            {
                "name": "CONFIG_SERVICE_URL",
                "value": f"https://{resource_prefix}-glaze.bakestack.com/api/config/rule/prd/latest"
            }
        ], 
        "jobName": "AWS-Data-Collector",
        "params": [
            {
                "encrypt": False,
                "value": "com.tmobile.cso.pacman",
                "key": "package_hint"},
                {
                    "encrypt": False,
                    "value": "dXNlcjpwYWNtYW4=",
                    "key": "config_creds"
                },
                {
                    "encrypt": False,
                    "value": account_id,
                    "key": "accountinfo"
                }
            ],
            "jobUuid": "pacman-aws-inventory-jar-with-dependencies",
            "jobDesc": "AWS-Data-Collection", "jobType": "jar"}
    get_lambda_client().invoke(
        FunctionName=f'{resource_prefix}-datacollector',
        InvocationType='RequestResponse',
        LogType='Tail',
        ClientContext=get_lambda_context(),
        Payload=json.dumps(event).encode()
    )

def get_lambda_context():
    client_context = dict(log_stream_name="empty")
    json_context = json.dumps(client_context).encode('utf-8')
    return base64.b64encode(json_context).decode('utf-8')

if __name__ == "__main__":
    handler(sys.argv)