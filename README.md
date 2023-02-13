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
