#TODO separate into its own module
from ..boto3_client import AWSClient

client = AWSClient(region='us-west-2', profile_name='sie-cloud-laco-platsvcs-nonprod-zz-sjohal',
                   service_name='cloudformation').get_client()

stack_resources = client.describe_stack_resources(StackName='hiraku-airflow2-nonprod')

resource_types = set(resource['ResourceType'] for resource in stack_resources['StackResources'])
print(resource_types)

# print(sorted(client.session.get_available_services()))
