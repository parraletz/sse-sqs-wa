from aws_cdk import (
    Duration,
    Stack,
)
from aws_cdk import aws_iam as iam

from aws_cdk.aws_lambda import Runtime
import  aws_cdk.aws_lambda_python_alpha as lambda_
from constructs import Construct 

class LambdaSseEnabled(Stack): 
    
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


        role = iam.Role(self, 'LambdaRole',
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )
        role.add_managed_policy(iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"))
        role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions= [
                'sqs:ListQueues',
                'sqs:SetQueueAttributes',
                'sqs:GetQueueAttributes',
                'sqs:GetQueueUrl'
            ],
            resources=["*"]
        ))

        handler = lambda_.PythonFunction(self,"SseSqsEnabled",
                entry="resource/sse_sqs_enabled",
                handler="handler",                   
                index='sse_sqs_enabled.py',
                runtime=Runtime.PYTHON_3_9,
                role=role
                                                
        )
        self._function_arn = handler.function_arn

    @property
    def handler_function_arn(self):
        print(self._function_arn)
        return self._function_arn
