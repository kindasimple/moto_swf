import unittest
from moto import mock_swf
import boto3
from service.client import get_client

@mock_swf()
def test_get_client():
    client = get_client()
    assert client is not None

def test_query_domains():
    client = boto3.client(
        service_name='swf',
        region_name='us-west-1',
        endpoint_url="http://localhost:5000"
    )
    #client.register_domain(name="test-domain", workflowExecutionRetentionPeriodInDays="1", description="A test domain")
    domains = client.list_domains(registrationStatus="REGISTERED")
    assert domains is not None
    assert len(domains["domainInfos"]) == 1
