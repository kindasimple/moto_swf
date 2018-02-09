import boto3
from moto import mock_swf

def get_client():
    client = boto3.client(       
        service_name='swf',
        region_name='us-west-1',
        endpoint_url="http://localhost:5000")
    return client
