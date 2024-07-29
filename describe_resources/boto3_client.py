"""
Create a boto3 session and return a client for the specified service
"""

import boto3


class AWSClient:
    def __init__(self, region, profile_name, service_name=None):
        self.region = region
        self.service_name = service_name
        self.session = boto3.session.Session(profile_name=profile_name, region_name=region)

    def get_client(self):
        client = self.session.client(self.service_name)
        return client


# test code
if __name__ == '__main__':
    client = AWSClient(region='us-west-2', profile_name='sie-cloud-laco-platsvcs-nonprod-zz-sjohal',
                       service_name='cloudformation').get_client()
    # client = AWSClient(region='us-west-2', profile_name='sie-cloud-laco-platsvcs-nonprod-zz-sjohal')

