from flask import Flask, request
import boto3
import os

app = Flask(__name__)

asu_id = "1233725170" 
s3_bucket = f"{asu_id}-in-bucket"
simpledb_domain = f"{asu_id}-simpleDB"
s3_client = boto3.client(
    's3', 
    region_name='us-east-1', 
    aws_access_key_id="",
    aws_secret_access_key=""
)
sdb_client = boto3.client(
    'sdb', 
    region_name='us-east-1', 
    aws_access_key_id="",
    aws_secret_access_key=""
)

@app.route('/', methods=['POST'])
def recognizeFace():
    
    file = request.files['inputFile']
    filename = os.path.splitext(file.filename)[0]

    s3_client.upload_fileobj(file, s3_bucket, filename)

    response = sdb_client.get_attributes(DomainName=simpledb_domain, ItemName=filename)
    attributes = response.get('Attributes', [])
    prediction = attributes[0]['Value']

    return f"{filename}:{prediction}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, threaded=True)
