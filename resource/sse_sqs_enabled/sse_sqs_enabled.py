import json
import cfnresponse
import boto3
import botocore.exceptions

def handler(event,context):
    print('Received request:\n%s' % json.dumps(event, indent=6))

    resource_properties = event['ResourceProperties']

    queue_url = event['ResourceProperties']['QueueUrl']

    if event['RequestType'] in ['Create', 'Update']:
        try: 
            client = boto3.client('sqs')
            response = client.set_queue_attributes(
                QueueUrl=queue_url,
                Attributes={'SqsManagedSseEnabled': 'true',}
            )
        except:
            cfnresponse.send(event, context, cfnresponse.FAILED, {})
            raise
        else:
            cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
    elif event['RequestType'] == 'Delete':
        cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
