# Table of Contents
1. [Description](#description)
2. [Main Features](#main-features)
3. [How to Use](#how-to-use)
4. [Maintenance](#maintenance)
7. [TODO](#todo)
5. [Use Cases](#use-cases)
6. [ROADMAP](#roadmap)


# Description
This was designed and implemented during PC22 Cafe-Day to catalogue all AWS resources in an account. It is a simple script that uses the AWS CLI to query all resources and then outputs the results to a JSON file.

## Main Features
1. Catalogue all AWS resources defined in a _stack_
2. Use the config file to 
   - control what attributes to catalogue
   - map the boto3 low-level client to the high-level resource

## How to Use
1. Install the AWS CLI v2
2. run `describe_stack_resources.py`


## Maintenance
1. When adding new stack, update config file:
   2. new boto3 low-level client to high-level resource mapping 
   3. new attributes to catalogue

---
### TODO
1. See other `TODO` comments in code
2. Sanitise the config file
3. Solidify the setup process
   - aws client config (e.g. select profile from local aws creds)
2. Try/catch and continue on error for new resources
2. Add more resources not deployed via stacks e.g. RDS
3. Log instead of print with debug option
4. Paramaterise `describe_stack_resources`
   - Maintain list of stacks
   - Which profile to use (use `xaws` instead)
5. Make more pythonic
   - Rename `instance` variable
   - Modularise e.g. `describe_instances.InstanceDescriber.describe_instances()`

---
## Use Cases
1. Detect and alert any drifts 
   - add to SLO 
   - vs. CFn drift remediation solutions using e.g. Lambda, see this [example]([url](https://aws.amazon.com/blogs/mt/implement-automatic-drift-remediation-for-aws-cloudformation-using-amazon-cloudwatch-and-aws-lambda/))
2. Catalogue all resources at a granularity we define and be in sync with any supporting architecture diagrams we publish to confluence
3. Could help with moderating what resources are not tagged or those that don't conform to prescribed standards
4. Compare across environments for _stack_X_


## ROADMAP
1. Starting point 
   - after we've tagged everything 
   - after we've reverse-engineered into stacks
      - what's the recursive level e.g. do we want to describle resources that hang off the resources delivered via the stack which pre-exist e.g. s3 buckets
   - Understand what are **all** of the resource types
   - Understand what configs we want to describe 
      - those that are billable
      - those not readily available via the UI
3. How and by whom should it be triggered (e.g. after we've tagged everything and/or after 
4. Define output 
   - that's digestable (currently nested so reverted to using json)
   - upload to e.g. Mongo DB
   - resource per tab
6. Should it be rebuilt or additive
7. Should it be scheduled (depends on the use case)
8. Should it be version controlled
9. Have a version that's public facing e.g. at a higher abstract level
