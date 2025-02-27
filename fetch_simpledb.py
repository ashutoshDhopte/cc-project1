import boto3
from pprint import pprint

client = boto3.client(
    'sdb', 
    region_name='us-east-1',
    aws_access_key_id="",
    aws_secret_access_key=""
)

asu_id = "1233725170"  # Replace with your actual ASU ID
domain_name = f"{asu_id}-simpleDB"

response = client.get_attributes(
    DomainName=domain_name,
    ItemName='test_100',
    ConsistentRead=True
)

pprint(response)