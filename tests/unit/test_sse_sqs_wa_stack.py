import aws_cdk as core
import aws_cdk.assertions as assertions

from sse_sqs_wa.sse_sqs_wa_stack import SseSqsWaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in sse_sqs_wa/sse_sqs_wa_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SseSqsWaStack(app, "sse-sqs-wa")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
