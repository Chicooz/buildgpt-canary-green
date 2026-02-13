import boto3

sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue'

# Send a message to the SQS queue
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody='Update docs request',
    MessageAttributes={
        'CodeOpsContext': {
            'StringValue': 'docs-update',
            'DataType': 'String'
        }
    }
)

print('Message ID:', response['MessageId'])