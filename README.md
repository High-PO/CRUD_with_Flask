# CRUD_with_Flask
API with CRUD functionality to store values ​​in DynamoDB

---

# Edit Part

```
...
# DynamoDB Profile Setup
dynamodb = boto3.resource("dynamodb", region_name='ap-northeast-2')
table = dynamodb.Table('test-dynamo')
...
```

- `'ap-northeast-2'` -> your region name
- `'test-dynamo'` -> your DynamoDB name

# Example

## GET Method

```
{
    "Name": "High-PO",
    "PN": "010-1234-5678"
}
```

## POST Method
```
{
    "Name": "High-PO",
    "PN": "010-1234-5678",
    "Zipcode": 12345
}
```
## PUT Method
```
{
    "Name": "High-PO",
    "PN": "010-1234-5678",
    "Zipcode": 67890
}
```
## DELETE Method
```
{
    "Name": "High-PO",
    "PN": "010-1234-5678"
}
```

# Health check path

## path
```
/health
```

## retrun value
```
{
    "status" : 200
}
```
