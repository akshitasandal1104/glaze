# CRAETE local.py file by renaming/copying default.local.py
# User should update the VPC details below in local.py
VPC = {
    "ID": "vpc-58a73b22",
    "CIDR_BLOCKS": ["172.31.0.0/16"],
    "SUBNETS": ["subnet-1fab9110", "subnet-4ee5aa60"]
}


# CUstom tags that can be defined by user
CUSTOM_RESOURCE_TAGS = {
    'Application': "PacBot",
    'Environment': "Prod",
    'Created By': "customer-name"
}


# RDS Related Configurations
RDS_INSTANCE_TYPE = "db.t3.micro"  # Possibble values db.m4.large, db.t2.large etc


# ElasticSearch Related Configurations
ES_INSTANCE_TYPE = "t2.small.elasticsearch"  # Possibble values m4.xlarge.elasticsearch, t2.xlarge.elasticsearch etc
ES_VOLUME_SIZE = 20

# ALB related configurations
MAKE_ALB_INTERNAL = False  # False if ALB need to be public(internet facing) else True
ALB_PROTOCOL = "HTTPS"
SSL_CERTIFICATE_ARN = "arn:aws:acm:us-east-1:325960980908:certificate/b19da35e-f2b7-4858-9c4e-f5013af92289"  # Required only if ALB_PROTOCOL is defined as HTTPS
PACBOT_DOMAIN = ""  # Required only if you point a CNAME record to ALB ex: app.pacbot.com
HOSTED_ZONE_NAME = "bakestack.com"

# MAIL Server configuration
MAIL_SERVER = "localhost"
MAIL_SERVER_PORT = 587
MAIL_PROTOCOL = "smtp"
MAIL_SERVER_USER = ""
MAIL_SERVER_PWD = ""
MAIL_SMTP_AUTH = ""
MAIL_SMTP_SSL_ENABLE = "true"
MAIL_SMTP_SSL_TEST_CONNECTION = "false"

USER_EMAIL_ID = ""

# System reads below data from user if not updated here
AWS_AUTH_MECHANISM = None  # Value should be numeric 1 or 2 or 3. I. If kept like this input is read from
# if AWS_AUTH_MECHANISM == 1
AWS_ACCESS_KEY = ""
AWS_SECRET_KEY = ""
AWS_REGION = ""
# If AWS_AUTH_MECHANISM == 2, AWS_ASSUME_ROLE_ARN is required
AWS_ASSUME_ROLE_ARN = ""

# This settings enable Vulnerability feature and servie
ENABLE_VULNERABILITY_FEATURE = True
QUALYS_API_URL = ""  # Qualys API Url without trailing slash
QUALYS_INFO = ""  # Base64 encoded user:password of qualys
# This settings enable Vulnerability feature and servie
ENABLE_AZURE = False
# Tenants should be a list of dict containing tenantId, clientId and secretId
AZURE_TENANTS = [
    {
        'tenantId': "t111",
        'clientId': "c111",
        'secretId': "s111"
    },
    {
        'tenantId': "t222",
        'clientId': "c222",
        'secretId': "s222"
    },
]
