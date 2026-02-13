import boto3

sqs = boto3.client('sqs')

queue_url = 'https://sqs.us-east-1.amazonaws.com/123456789012/MyQueue'

# Poll for messages from the SQS queue
while True:
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10,
        MessageAttributeNames=['All']
    )

    messages = response.get('Messages', [])

    for message in messages:
        code_ops_context = message['MessageAttributes'].get('CodeOpsContext', {}).get('StringValue')
        if code_ops_context == 'docs-update':
            print('Applying docs update...')
            # Logic to apply the docs update
            
            # Delete the message after processing
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=message['ReceiptHandle']
            )

    if not messages:
        print('No messages to process.')