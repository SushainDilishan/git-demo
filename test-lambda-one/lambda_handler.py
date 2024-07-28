import json

def lambda_handler(event, context):
    print("woahhh")
    print("Testing a new commit")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }