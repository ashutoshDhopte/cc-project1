import requests
import os

image_path = "face_images_1000/test_002.jpg"
file = {"inputFile": open(image_path,'rb')}
# url = "http://3.211.100.35:8000"
url = "http://localhost:8000"
response = requests.post(url, files=file)
# Print error message if failed
if response.status_code != 200:
    print('sendErr: '+response.url)
else :
    filename    = os.path.basename(image_path)
    image_msg   = filename + ' uploaded!'
    msg         = image_msg + '\n' + 'Classification result: ' + response.text
    print(msg)