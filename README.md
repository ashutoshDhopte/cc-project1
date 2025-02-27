# Cloud Computing Project 1

This project introduces AWS and demonstrates how to leverage EC2 instances and storage like S3 and SimpleDB to create a server for lightweight multi-threaded APIs. 

## Tech Stack
Language: Python
Server: AWS EC2, AWS S3, AWS SimpleDB
Libraries: Boto3, Flask

## Flow

### create_simple_db.py
This is used to create a new database in SimpleDB and upload information of all the pictures in a Key-Value format.

### server.py
This is used to create a Flask API and is hosted on an EC2 instance. It gets a post request from the client with an image in the payload. It extracts the file's name, uploads the image to the S3 bucket, searches the name in the SimpleDB, and returns the value.

The Flask API uses "threaded=True" to make it multi-threaded, i.e., the API will process multiple client requests simultaneously. 
