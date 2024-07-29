from typing import List, Any

from botocore.client import BaseClient

from boto3_client import AWSClient

profile = 'dummyprofile'

def describe_stack_resources(stack_name):
    """
    Returns a list of dictionaries describing the resources in the specified CloudFormation stack
    """
    client = AWSClient(region='us-west-2', profile_name=profile,
                       # TODO parameterize
                       service_name='cloudformation').get_client()

    # get the list of stack resources
    response = client.describe_stack_resources(StackName=stack_name)
    stack_resources = response['StackResources']

    # create a list of dictionaries describing each resource
    resources = []
    for resource in stack_resources:
        resource_type = resource['ResourceType']
        physical_resource_id = resource['PhysicalResourceId']
        resource_status = resource['ResourceStatus']
        resource_dict = {
            'Type': resource_type,
            'PhysicalResourceId': physical_resource_id,
            'Status': resource_status
        }
        resources.append(resource_dict)

    return resources


if __name__ == '__main__':
    from config import resourcetype_to_service_dict, describe_attrs_json
    from describe_resources import InstanceDescriber

    # hyper parameters
    profile = 'nonprod-zz-sjohal'
    debug_mode = True
    tag_value = 'airflow'
    stack_list = ['airflow-nonprod', 'slo-nonprod']


    # TODO use logger instead of print
    def print_console(type, msg=None):
        if debug_mode:
            print(f"{type}: {msg}")


    # loop through all stacks
    for stack in stack_list:
        print_console('****stack****', stack)
        resources = describe_stack_resources(stack)

        # loop through all resources in the stack
        for resource in resources:
            resource_service_type = resource['Type']
            resource_physical_id = resource['PhysicalResourceId']

            # create another boto3 low-level client for the resource type using the config.resourcetype_to_service_dict
            boto3_client_type = resourcetype_to_service_dict[resource_service_type][0]
            boto3_client_servicetype = resourcetype_to_service_dict[resource_service_type][1]

            print_console('****boto3_client_type****', boto3_client_type)
            print_console('\tresource_service_type', resource_service_type)
            print_console('\tresource_physical_id', resource_physical_id)

            # if boto3_client_type == 'ec2' and resource_service_type == 'AWS::EC2::Instance':
            # if boto3_client_type == 'elbv2' and resource_service_type == 'AWS::ElasticLoadBalancingV2::LoadBalancer':
            # if boto3_client_type == 'elbv2' and resource_service_type == 'AWS::ElasticLoadBalancingV2::Listener':
            # if boto3_client_type == 'elbv2' and resource_service_type == 'AWS::ElasticLoadBalancingV2::TargetGroup':
            instance_describer = InstanceDescriber(region='us-west-2',
                                                   profile_name=profile,
                                                   service_name=boto3_client_type,
                                                   filter_dict=describe_attrs_json[boto3_client_type][
                                                          boto3_client_servicetype],
                                                   service_type=resource_service_type,
                                                   physical_resource_id=[resource_physical_id],
                                                   stack_name=stack
                                                   )

            instance_describer.describe_and_print_instances(tag_key='Service', tag_value=tag_value,
                                                            attributes=describe_attrs_json[boto3_client_type][
                                                                boto3_client_servicetype])

    # describe resources not in stacks
    # EMR, RDS
    from boto3_client import AWSClient

    resource_service_type = 'AWS::EMR::Cluster'
    emr_client: BaseClient = AWSClient(region='us-west-2', profile_name=profile, service_name='emr').get_client()
    response = emr_client.list_clusters(ClusterStates=['WAITING'])

    resource_physical_ids: list[Any] = []
    for cluster in response['Clusters']:
        resource_physical_ids.append(cluster['Id'])
    # resource_physical_ids = response['Clusters'][0]

    for resource_physical_id in resource_physical_ids:
        boto3_client_type = resourcetype_to_service_dict[resource_service_type][0]
        boto3_client_servicetype = resourcetype_to_service_dict[resource_service_type][1]

        instance_describer = InstanceDescriber(region='us-west-2',
                                               profile_name=profile,
                                               service_name=boto3_client_type,
                                               filter_dict=describe_attrs_json[boto3_client_type][
                                                   boto3_client_servicetype],
                                               service_type=resource_service_type,
                                               physical_resource_id=[resource_physical_id],
                                               stack_name='None-EMR'
                                               )

        instance_describer.describe_and_print_instances(tag_key='Service', tag_value=tag_value,
                                                        attributes=describe_attrs_json[boto3_client_type][
                                                            boto3_client_servicetype])
