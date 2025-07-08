import boto3, json, os
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')
table = dynamodb.Table(os.environ['TABLE_NAME'])
topic_arn = os.environ['TOPIC_ARN']

def lambda_handler(event, context):
    body = json.loads(event['body'])
    item = {
        'objectId': str(uuid4()),
        'data': body.get('data', 'No data')
    }
    table.put_item(Item=item)
    sns.publish(TopicArn=topic_arn, Message=json.dumps(item))
    return {"statusCode": 200, "body": json.dumps(item)}
