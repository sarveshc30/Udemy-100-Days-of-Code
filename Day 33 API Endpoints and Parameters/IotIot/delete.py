import requests
import json
from requests.auth import HTTPBasicAuth

with open(r'F:\IotIot\Resources\credentials.txt' , 'r') as file:
    credentials = json.load(file)

print(credentials)