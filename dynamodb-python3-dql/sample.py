import dql
import boto3
import os
table_name=os.environ['TABLE_NAME'] # dynamodb


engine = dql.Engine()
c = engine.connect(
    region=os.environ['AWS_DEFAULT_REGION'],
    access_key=os.environ['AWS_ACCESS_KEY_ID'],
    secret_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    host=os.environ['HOST'],
    port=int(os.environ['PORT']),
    is_secure=False
)
print("--scan--")
results = engine.execute(f"SCAN * FROM {table_name} LIMIT 10")
for item in results:
    print(dict(item))

print("--delete--")
results = engine.execute(f"DELETE FROM {table_name} WHERE tm>=1235 and tm<=1236")

print("--scan--")
results = engine.execute(f"SCAN * FROM {table_name} LIMIT 10")
for item in results:
    print(dict(item))