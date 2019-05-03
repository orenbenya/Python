#downloading the needed file from S3 bucket
import boto3
import botocore
import subprocess
import urllib3
import simplejson as json

Bucket = "BUCKET_NAME"
Key = "FILE_NAME.tar.gz"
DLfileName = "FILE_NAME.tar.gz"

s3 = boto3.resource('s3')
try:
    s3.Bucket(Bucket).download_file(Key, DLfileName)
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

#building the app using docker compose
subprocess.run(["sudo", "docker-compose", "up", "-d", "--build"])

# checking http code of the app /health
http = urllib3.PoolManager()
r = http.request('GET', 'localhost:3000/health')
print(json.dumps({'http code': r.status}, indent=4 * ' '))

a = r.status
b = 200
while b == r.status:
  print("service is up & running")
  break
else:
 print("service is down")
exit(1)
