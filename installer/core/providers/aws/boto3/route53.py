from botocore.exceptions import ClientError
from core.providers.aws.boto3 import prepare_aws_client_with_given_cred
from core.config import Settings
import boto3


def get_route53_client(aws_auth_cred):
    """ return boto client"""
    if aws_auth_cred:
        if aws_auth_cred.get("aws_auth_option") == 3:
            return boto3.client("route53", aws_auth_cred.get("aws_region"))
    return boto3.client("route53", aws_auth_cred)

def get_elbv2_client(aws_auth_cred):
    """ return boto client"""
    if aws_auth_cred:
        if aws_auth_cred.get("aws_auth_option") == 3:
            return boto3.client("elbv2", aws_auth_cred.get("aws_region"))
    return boto3.client("elbv2", aws_auth_cred)


def add_cname_record(aws_auth_cred=None):
        """creates CNAME record as a route53 entry for hosted zone, bakestack.com"""
        hosted_zone_id = get_hosted_zone_id(Settings.get("HOSTED_ZONE_NAME"), aws_auth_cred)
        record_name = Settings.get("PACBOT_DOMAIN")
        value = get_alb_url(aws_auth_cred)
        record = {
            "Changes": [
                {
                    "Action": "CREATE",
                    "ResourceRecordSet": {
                        "Name": record_name,
                        "Type": "CNAME",
                        "ResourceRecords": [{
                                "Value": value
                            }
                        ],
                        "TTL": 300
                    }
                }
            ]
        }
        get_route53_client(aws_auth_cred).change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch=record
        )

def delete_cname_record(aws_auth_cred=None):
        """creates CNAME record as a route53 entry for hosted zone, bakestack.com"""
        hosted_zone_id = get_hosted_zone_id(Settings.get("HOSTED_ZONE_NAME"), aws_auth_cred)
        record_name = Settings.get("PACBOT_DOMAIN")
        value = get_alb_url(aws_auth_cred)
        record = {
            "Changes": [
                {
                    "Action": "DELETE",
                    "ResourceRecordSet": {
                        "Name": record_name,
                        "Type": "CNAME",
                        "ResourceRecords": [{
                                "Value": value
                            }
                        ],
                        "TTL": 300
                    }
                }
            ]
        }
        try:
            get_route53_client(aws_auth_cred).change_resource_record_sets(
                HostedZoneId=hosted_zone_id,
                ChangeBatch=record
            )
        except ClientError as client_error:
            error = client_error.response.get("Error")
            if error.get("Code") == "InvalidChangeBatch":
                if "was not found" not in error.get("Message"):
                    raise client_error


def get_hosted_zone_id(name, aws_auth_cred=None):
    """ gets the r53 hosted zone ID fron name"""
    return get_route53_client(aws_auth_cred).list_hosted_zones_by_name(
        DNSName=name,
        MaxItems="1"
    ).get("HostedZones")[0].get("Id")

def get_alb_url(aws_auth_cred):
    """ """
    return get_elbv2_client(aws_auth_cred).describe_load_balancers(
        Names=[Settings.get("RESOURCE_NAME_PREFIX")]
    ).get("LoadBalancers")[0].get("DNSName")