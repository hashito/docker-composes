import dql
import boto3
import os
#import dynamo3
table_name=os.environ['TABLE_NAME'] # dynamodb
#end_point=os.environ['END_POINT']   # http://172.19.0.3:8000
#dynamodb = boto3.resource('dynamodb',endpoint_url=end_point)
#table = dynamodb.Table(table_name)


engine = dql.Engine()
c = engine.connect(
#    session=boto3.Session(),
    region=os.environ['AWS_DEFAULT_REGION'],
    access_key=os.environ['AWS_ACCESS_KEY_ID'],
    secret_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    host=os.environ['HOST'],
    port=int(os.environ['PORT']),
    is_secure=False
)
print("--scan--")
#    def connect(cls, region, session=None, access_key=None, secret_key=None,
#                host=None, port=80, is_secure=True, **kwargs):
#results = engine.execute(f"SELECT * FROM {table_name} LIMIT 10")
results = engine.execute(f"SCAN * FROM {table_name} LIMIT 10")
for item in results:
    print(dict(item))

print("--delete--")
results = engine.execute(f"DELETE FROM {table_name} WHERE tm>=1235 and tm<=1236")

print("--scan--")
results = engine.execute(f"SCAN * FROM {table_name} LIMIT 10")
for item in results:
    print(dict(item))

