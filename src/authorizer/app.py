def lambda_handler(event, context):
    token = event['authorizationToken']
    if token == "allow123":
        return {
            "principalId": "user",
            "policyDocument": {
                "Version": "2012-10-17",
                "Statement": [{
                    "Action": "execute-api:Invoke",
                    "Effect": "Allow",
                    "Resource": event['methodArn']
                }]
            }
        }
    raise Exception("Unauthorized")
