import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "ten-examples-dynamodb-boto3"

# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb', region_name="us-west-2")

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', region_name="us-west-2")
table = dynamodb.Table(TABLE_NAME)

# Use the DynamoDB client query method to get songs by artist Arturus Ardvarkian
# that have a song attribute value BETWEEN 'D' and 'Bz'
response = dynamodb_client.query(
    TableName=TABLE_NAME,
    KeyConditionExpression='artist = :artist AND song BETWEEN :songval1 AND :songval2',
    ExpressionAttributeValues={
        ':artist': {'S': 'Arturus Ardvarkian'},
        ':songval1': {'S': 'Bz'},
        ':songval2': {'S': 'D'}
    }
)
print(response['Items'])
