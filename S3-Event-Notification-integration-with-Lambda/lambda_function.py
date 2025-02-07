import json
import urllib.parse
import boto3

# This lambda just reads the file uploaded to the specific buckets whose notification events are
# configured to trigger the lambda.

def lambda_handler(event, context):

    ObjectName = event['Records'][0]['s3']['object']['key']
    BucketName = event['Records'][0]['s3']['bucket']['name']

    print(f'Object Name: {ObjectName}, Uploaded to {BucketName}')

    # reading the content in the object
    s3 = boto3.client('s3')
    try:
        obj = s3.get_object(Bucket=BucketName, Key=ObjectName)
    except Exception as e:
        print(f'Error getting object {ObjectName} from bucket {BucketName}. Make sure they exist and your bucket is in the same region as this function.')
        raise e
    try:
        content = obj['Body'].read().decode('utf-8')
        print(f'Content: {content}')
    except Exception as e:
        print(f'Error reading object\'s body: {ObjectName}')
        raise e