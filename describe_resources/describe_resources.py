from typing import List, Dict
import json
from boto3_client import AWSClient
import pandas as pd
import os
from datetime import datetime

stackName = 'dummyvalue'


class InstanceDescriber:
    def __init__(self, region: str, profile_name: str, service_name: str, filter_dict: Dict, service_type: str,
                 physical_resource_id: list, stack_name: str):
        self.client = AWSClient(region=region, profile_name=profile_name,
                                service_name=service_name).get_client()
        self.filter_json = json.dumps(filter_dict, default=str)
        self.service_name = service_name
        self.service_type = service_type
        self.physical_resource_id = physical_resource_id
        self.stack_name = stack_name

    def describe_instances(self, tag_key: str, tag_value: str, attributes: List[str]) -> List[Dict[str, str]]:
        global response
        filter = [
            {
                'Name': f'tag:{tag_key}',
                'Values': [
                    stackName,
                ]
            },
        ]

        #TODO combine the 2 sections below and modularise
        if self.service_name == 'ec2':
            response = self.client.describe_instances(Filters=filter)
        elif self.service_name == 'elbv2' and self.service_type == 'AWS::ElasticLoadBalancingV2::LoadBalancer':
            response = self.client.describe_load_balancers(LoadBalancerArns=self.physical_resource_id)
        elif self.service_name == 'elbv2' and self.service_type == 'AWS::ElasticLoadBalancingV2::Listener':
            response = self.client.describe_listeners(ListenerArns=self.physical_resource_id)
        elif self.service_name == 'elbv2' and self.service_type == 'AWS::ElasticLoadBalancingV2::TargetGroup':
            response = self.client.describe_target_groups(TargetGroupArns=self.physical_resource_id)
        elif self.service_name == 'cloudwatch' and self.service_type == 'AWS::CloudWatch::Dashboard':
            # response = self.client.get_dashboard(DashboardName=self.physical_resource_id[0])
            response = self.client.list_dashboards(DashboardNamePrefix='hiraku') ##TODO need to serialise LastModified
        elif self.service_name == 'cloudwatch' and self.service_type == 'AWS::CloudWatch::Alarm':
            response = self.client.describe_alarms(AlarmNames=self.physical_resource_id)
        elif self.service_name == 'emr' and self.service_type == 'AWS::EMR::Cluster':
            response = self.client.describe_cluster(ClusterId=self.physical_resource_id[0])

        matching_instances = []
        if self.service_name == 'ec2':
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    matching_instance = {}
                    for attribute in attributes:
                        matching_instance[attribute] = instance.get(attribute, 'N/A')
                    matching_instances.append(matching_instance)
        elif self.service_name == 'elbv2' and self.service_type == 'AWS::ElasticLoadBalancingV2::LoadBalancer':
            for load_balancer in response['LoadBalancers']:
                matching_instance = {}
                for attribute in attributes:
                    matching_instance[attribute] = load_balancer.get(attribute, 'N/A')
                matching_instances.append(matching_instance)
        elif self.service_name == 'elbv2' and self.service_type == 'AWS::ElasticLoadBalancingV2::Listener':
            for listener in response['Listeners']:
                matching_instance = {}
                for attribute in attributes:
                    matching_instance[attribute] = listener.get(attribute, 'N/A')
                matching_instances.append(matching_instance)
        elif self.service_name == 'elbv2' and self.service_type == 'AWS::ElasticLoadBalancingV2::TargetGroup':
            for target_group in response['TargetGroups']:
                matching_instance = {}
                for attribute in attributes:
                    matching_instance[attribute] = target_group.get(attribute, 'N/A')
                matching_instances.append(matching_instance)
        elif self.service_name == 'cloudwatch' and self.service_type == 'AWS::CloudWatch::Dashboard':
            for dashboard in response['DashboardEntries']:
                matching_instance = {}
                for attribute in attributes:
                    matching_instance[attribute] = dashboard.get(attribute, 'N/A')
                matching_instances.append(matching_instance)
        elif self.service_name == 'cloudwatch' and self.service_type == 'AWS::CloudWatch::Alarm':
            for alarm in response['MetricAlarms']:
                matching_instance = {}
                for attribute in attributes:
                    matching_instance[attribute] = alarm.get(attribute, 'N/A')
                matching_instances.append(matching_instance)
        elif self.service_name == 'emr' and self.service_type == 'AWS::EMR::Cluster':
            matching_instance = {}
            for attribute in attributes:
                matching_instance[attribute] = response['Cluster'].get(attribute, 'N/A')
            matching_instances.append(matching_instance)

        return matching_instances

    def print_instance_attributes(self, instance: Dict):
        for key in instance:
            print(f"{key}: {instance[key]}")

    # Write to a local excel file located in ./output with a tab per service type as if executed from describe_and_print_instances
    def write_to_excel(self, instance: Dict):
        # df = pd.DataFrame(instance, index=[0])
        df = pd.DataFrame.from_dict(instance, orient='index')
        writer = pd.ExcelWriter(f'./output/{self.service_name}.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name=self.service_name, index=False)
        writer.save()


    # Define a function to serialise datetime objects to strings
    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""
        if isinstance(obj, (datetime)):
            return obj.isoformat()
        raise TypeError("Type %s not serializable" % type(obj))

    # Write to a local json file located in ./output per service name and service type as if executed from describe_and_print_instances
    def write_to_json(self, instance: Dict):
        global stack_dir
        main_dir = './output'

        # create a directory for that stack name if it doesn't exist
        stack_dir = f'{main_dir}/{self.stack_name}'
        if not os.path.exists(f'{main_dir}/{self.stack_name}'):
            os.makedirs(stack_dir)

        # Create a subdirectory with the current date and time as its name
        sub_dir = datetime.now().strftime("%Y-%m-%d")
        full_path = os.path.join(main_dir, stack_dir, sub_dir)
        if not os.path.exists(full_path):
            os.makedirs(full_path)

        full_path_name = f'{full_path}/{self.service_name}__{self.service_type}.json'

        # Check if the file exists then create another using the 1st key in the instance dict
        if os.path.exists(full_path_name):
            service_type_name = list(instance.values())[:1][0]
            full_path_name = f'{full_path}/{self.service_name}__{self.service_type}_{service_type_name}.json'

        try:
            with open(full_path_name, 'w') as f:
                json.dump(instance, f, indent=4)
                # json.dumps(instance, indent=4, default=self.json_serial)
                # json.dumps(instance, indent=4, default=lambda x: self.json_serial(x))
        except Exception as e:
            print(e)


    def describe_and_print_instances(self, tag_key: str, tag_value: str, attributes: List[str]):
        matching_instances = self.describe_instances(tag_key, tag_value, attributes)
        for instance in matching_instances:
            # self.print_instance_attributes(instance)
            # self.write_to_excel(instance) #TODO need to expand this to write to a tab per service type
            self.write_to_json(instance)

