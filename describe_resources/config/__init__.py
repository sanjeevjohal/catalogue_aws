available_services_list = ['accessanalyzer', 'account', 'acm', 'acm-pca', 'alexaforbusiness', 'amp', 'amplify',
                           'amplifybackend', 'amplifyuibuilder', 'apigateway', 'apigatewaymanagementapi',
                           'apigatewayv2', 'appconfig', 'appconfigdata', 'appflow', 'appintegrations',
                           'application-autoscaling', 'application-insights', 'applicationcostprofiler', 'appmesh',
                           'apprunner', 'appstream', 'appsync', 'arc-zonal-shift', 'athena', 'auditmanager',
                           'autoscaling', 'autoscaling-plans', 'backup', 'backup-gateway', 'backupstorage', 'batch',
                           'billingconductor', 'braket', 'budgets', 'ce', 'chime', 'chime-sdk-identity',
                           'chime-sdk-media-pipelines', 'chime-sdk-meetings', 'chime-sdk-messaging', 'chime-sdk-voice',
                           'cleanrooms', 'cloud9', 'cloudcontrol', 'clouddirectory', 'cloudformation', 'cloudfront',
                           'cloudhsm', 'cloudhsmv2', 'cloudsearch', 'cloudsearchdomain', 'cloudtrail', 'cloudwatch',
                           'codeartifact', 'codebuild', 'codecatalyst', 'codecommit', 'codedeploy', 'codeguru-reviewer',
                           'codeguruprofiler', 'codepipeline', 'codestar', 'codestar-connections',
                           'codestar-notifications', 'cognito-identity', 'cognito-idp', 'cognito-sync', 'comprehend',
                           'comprehendmedical', 'compute-optimizer', 'config', 'connect', 'connect-contact-lens',
                           'connectcampaigns', 'connectcases', 'connectparticipant', 'controltower', 'cur',
                           'customer-profiles', 'databrew', 'dataexchange', 'datapipeline', 'datasync', 'dax',
                           'detective', 'devicefarm', 'devops-guru', 'directconnect', 'discovery', 'dlm', 'dms',
                           'docdb', 'docdb-elastic', 'drs', 'ds', 'dynamodb', 'dynamodbstreams', 'ebs', 'ec2',
                           'ec2-instance-connect', 'ecr', 'ecr-public', 'ecs', 'efs', 'eks', 'elastic-inference',
                           'elasticache', 'elasticbeanstalk', 'elastictranscoder', 'elb', 'elbv2', 'emr',
                           'emr-containers', 'emr-serverless', 'es', 'events', 'evidently', 'finspace', 'finspace-data',
                           'firehose', 'fis', 'fms', 'forecast', 'forecastquery', 'frauddetector', 'fsx', 'gamelift',
                           'gamesparks', 'glacier', 'globalaccelerator', 'glue', 'grafana', 'greengrass',
                           'greengrassv2', 'groundstation', 'guardduty', 'health', 'healthlake', 'honeycode', 'iam',
                           'identitystore', 'imagebuilder', 'importexport', 'inspector', 'inspector2', 'iot',
                           'iot-data', 'iot-jobs-data', 'iot-roborunner', 'iot1click-devices', 'iot1click-projects',
                           'iotanalytics', 'iotdeviceadvisor', 'iotevents', 'iotevents-data', 'iotfleethub',
                           'iotfleetwise', 'iotsecuretunneling', 'iotsitewise', 'iotthingsgraph', 'iottwinmaker',
                           'iotwireless', 'ivs', 'ivschat', 'kafka', 'kafkaconnect', 'kendra', 'kendra-ranking',
                           'keyspaces', 'kinesis', 'kinesis-video-archived-media', 'kinesis-video-media',
                           'kinesis-video-signaling', 'kinesis-video-webrtc-storage', 'kinesisanalytics',
                           'kinesisanalyticsv2', 'kinesisvideo', 'kms', 'lakeformation', 'lambda', 'lex-models',
                           'lex-runtime', 'lexv2-models', 'lexv2-runtime', 'license-manager',
                           'license-manager-linux-subscriptions', 'license-manager-user-subscriptions', 'lightsail',
                           'location', 'logs', 'lookoutequipment', 'lookoutmetrics', 'lookoutvision', 'm2',
                           'machinelearning', 'macie', 'macie2', 'managedblockchain', 'marketplace-catalog',
                           'marketplace-entitlement', 'marketplacecommerceanalytics', 'mediaconnect', 'mediaconvert',
                           'medialive', 'mediapackage', 'mediapackage-vod', 'mediastore', 'mediastore-data',
                           'mediatailor', 'memorydb', 'meteringmarketplace', 'mgh', 'mgn',
                           'migration-hub-refactor-spaces', 'migrationhub-config', 'migrationhuborchestrator',
                           'migrationhubstrategy', 'mobile', 'mq', 'mturk', 'mwaa', 'neptune', 'network-firewall',
                           'networkmanager', 'nimble', 'oam', 'omics', 'opensearch', 'opensearchserverless', 'opsworks',
                           'opsworkscm', 'organizations', 'outposts', 'panorama', 'personalize', 'personalize-events',
                           'personalize-runtime', 'pi', 'pinpoint', 'pinpoint-email', 'pinpoint-sms-voice',
                           'pinpoint-sms-voice-v2', 'pipes', 'polly', 'pricing', 'privatenetworks', 'proton', 'qldb',
                           'qldb-session', 'quicksight', 'ram', 'rbin', 'rds', 'rds-data', 'redshift', 'redshift-data',
                           'redshift-serverless', 'rekognition', 'resiliencehub', 'resource-explorer-2',
                           'resource-groups', 'resourcegroupstaggingapi', 'robomaker', 'rolesanywhere', 'route53',
                           'route53-recovery-cluster', 'route53-recovery-control-config', 'route53-recovery-readiness',
                           'route53domains', 'route53resolver', 'rum', 's3', 's3control', 's3outposts', 'sagemaker',
                           'sagemaker-a2i-runtime', 'sagemaker-edge', 'sagemaker-featurestore-runtime',
                           'sagemaker-geospatial', 'sagemaker-metrics', 'sagemaker-runtime', 'savingsplans',
                           'scheduler', 'schemas', 'sdb', 'secretsmanager', 'securityhub', 'securitylake',
                           'serverlessrepo', 'service-quotas', 'servicecatalog', 'servicecatalog-appregistry',
                           'servicediscovery', 'ses', 'sesv2', 'shield', 'signer', 'simspaceweaver', 'sms', 'sms-voice',
                           'snow-device-management', 'snowball', 'sns', 'sqs', 'ssm', 'ssm-contacts', 'ssm-incidents',
                           'ssm-sap', 'sso', 'sso-admin', 'sso-oidc', 'stepfunctions', 'storagegateway', 'sts',
                           'support', 'support-app', 'swf', 'synthetics', 'textract', 'timestream-query',
                           'timestream-write', 'transcribe', 'transfer', 'translate', 'voice-id', 'waf', 'waf-regional',
                           'wafv2', 'wellarchitected', 'wisdom', 'workdocs', 'worklink', 'workmail',
                           'workmailmessageflow', 'workspaces', 'workspaces-web', 'xray']

describe_attrs_json = {
    'ec2': {
        'EC2Attributes': {
            "InstanceId": "",
            "InstanceType": "",
            "KeyName": "",
            "SecurityGroups": [],
            "PublicIpAddress": "",
            "PrivateIpAddress": "",
            "Tags": []
        }
    },
    'elbv2': {
        'LoadBalancerAttributes': {
            "LoadBalancerArn": "",
            "LoadBalancerName": "",
            "Scheme": "",
            "VpcId": "",
            "AvailabilityZones": [],
            "SecurityGroups": [],
            "Subnets": []
        },
        'ListenerAttributes': {
            "ListenerArn": "",
            "LoadBalancerArn": "",
            "Port": "",
            "Protocol": "",
            "Certificates": [],
            "SslPolicy": ""
        },
        'TargetGroupAttributes': {
            "TargetGroupArn": "",
            "TargetGroupName": "",
            "Protocol": "",
            "Port": "",
            "VpcId": "",
            "HealthCheckProtocol": "",
            "HealthCheckPort": "",
            "HealthCheckEnabled": "",
            "HealthCheckIntervalSeconds": ""
        }
    },
    'cloudwatch': {
        'DashboardAttributes': {
            "DashboardName": "",
            "DashboardArn": "",
            "LastModified": ""
        },
        'AlarmAttributes': {
            "AlarmName": "",
            "AlarmArn": "",
            "AlarmDescription": "",
            # "AlarmConfigurationUpdatedTimestamp": "", ##TODO need to serialize this
            "ActionsEnabled": "",
            "OKActions": [],
            "AlarmActions": [],
            "InsufficientDataActions": [],
            "StateValue": "",
            "StateReason": ""
        }
    },
    'emr': {
        'ClusterAttributes': {
            "Id": "",
            "Name": "",
            "NormalizedInstanceHours": "",
            "MasterPublicDnsName": "",
            "Configurations": [],
        }
    }
}

# create a dictionary to map these resource type services to the available services
resourcetype_to_service_dict = {
    'AWS::EC2::Instance': ['ec2', 'EC2Attributes'],
    'AWS::ElasticLoadBalancingV2::LoadBalancer': ['elbv2', 'LoadBalancerAttributes'],
    'AWS::ElasticLoadBalancingV2::Listener': ['elbv2', 'ListenerAttributes'],
    'AWS::ElasticLoadBalancingV2::TargetGroup': ['elbv2', 'TargetGroupAttributes'],
    'AWS::CloudWatch::Dashboard': ['cloudwatch', 'DashboardAttributes'],
    'AWS::CloudWatch::Alarm': ['cloudwatch', 'AlarmAttributes'],
    'AWS::EMR::Cluster': ['emr', 'ClusterAttributes']
}
