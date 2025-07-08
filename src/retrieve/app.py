import boto3, os, json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])

def lambda_handler(event, context):
    response = table.scan()
    return {"statusCode": 200, "body": json.dumps(response.get('Items', []))}
