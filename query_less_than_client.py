import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "ten-examples-dynamodb-boto3"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="us-west-2")

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="us-west-2")
table = dynamodb.Table(TABLE_NAME)

response = dynamodb_client.query(
    TableName=TABLE_NAME,
    KeyConditionExpression='artist = :artist AND song < :song',
    ExpressionAttributeValues={
        ':artist': {'S': 'Arturus Ardvarkian'},
        ':song': {'S': 'C'}
    }
)
print(response['Items'])
