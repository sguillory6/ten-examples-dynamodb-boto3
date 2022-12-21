import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "ten-examples-dynamodb-boto3"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="us-west-2")

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="us-west-2")
table = dynamodb.Table(TABLE_NAME)

# Use the DynamoDB client query method to get songs by artist Arturus Ardvarkian
# that start with "C"
response = dynamodb_client.query(
    TableName=TABLE_NAME,
    KeyConditionExpression='artist = :artist AND begins_with ( song , :song )',
    ExpressionAttributeValues={
        ':artist': {'S': 'Arturus Ardvarkian'},
        ':song': {'S': 'C'}
    }
)
print(response['Items'])
