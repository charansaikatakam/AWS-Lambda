import boto3
import json
import os
import uuid

table_name = os.environ['TABLE_NAME']
baseUrl = os.environ['BASE_URL']

def shortenUrl(url):
    shortId = str(uuid.uuid4())[:6]
    return shortId

def lambda_handler(event, context):

    if 'url' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps('No url provided')
        }
    
    longUrl = event['url']
    shortId = shortenUrl(longUrl)
    shortUrl = f'{baseUrl}/{shortId}'
    print(f'longurl - {longUrl}, shortid - {shortId}, shortUrl - {shortUrl}')

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('table_name')

    response = table.put_item(
        TableName=table_name,
        Item={
            'short_id': shortId,
            'long_url': longUrl
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps({
            'shortUrl': shortUrl
        })
    }