from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_cloudformation as cfn
)
from constructs import Construct

class SseSqsWaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, lambda_arn: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        

        queue = sqs.Queue(
         self, "SseSqsWaQueue",
         visibility_timeout=Duration.seconds(300),

        )


        sse_sqs_enabled = cfn.CfnCustomResource(self, "SQSSseSqsEnabled",
            service_token=lambda_arn
        )
        sse_sqs_enabled.add_override(
            "Properties.QueueUrl", queue.queue_url
        )


#         cfn_wait_condition_handle = cfn.CfnWaitConditionHandle(self,'WaitConditionHandle')
        # cfn_wait_condition = cfn.CfnWaitCondition(self,"MyCfnWaitCondition",
           # count=1,
           # handle=cfn_wait_condition_handle.ref, 
           # timeout="600"           
        # )
        
