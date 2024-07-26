import json

def lambda_handler(event, context):
    print("woahhh")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }