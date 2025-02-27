import boto3
import csv

client = boto3.client(
    'sdb', 
    region_name='us-east-1',
    aws_access_key_id="",
    aws_secret_access_key=""
)

asu_id = "1233725170"  # Replace with your actual ASU ID
domain_name = f"{asu_id}-simpleDB"

client.create_domain(DomainName=domain_name)
print(f"Created SimpleDB domain: {domain_name}")


def populate_simpledb():
    with open('Classification Results on Face Dataset (1000 images).csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            filename, prediction = row[0], row[1]
            client.put_attributes(
                DomainName=domain_name,
                ItemName=filename,
                Attributes=[{'Name': 'prediction', 'Value': prediction, 'Replace': True}]
            )
    print("SimpleDB populated with face recognition data.")

populate_simpledb()
