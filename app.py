#!/usr/bin/env python3
import os

import aws_cdk as cdk

from sse_sqs_wa.sse_sqs_wa_stack import SseSqsWaStack
from lambda_custom_resource.sse_sqs_enabled import LambdaSseEnabled

env = cdk.Environment(account="694277229149", region="us-west-2")

app = cdk.App()
lambda_custom_resource = LambdaSseEnabled(app, "LambdaSseEnabled", env=env)

sqs_stack = SseSqsWaStack(app, "SseSqsWaStack-3", env=env,
    lambda_arn=lambda_custom_resource.handler_function_arn
    )

app.synth()
