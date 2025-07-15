import requests
import json
from requests.auth import HTTPBasicAuth

# GET Request
session = requests.session()
URL = "https://beelinkdirect.com/wp-json/wp/v2/posts?_fields=id,title,content&page=1"
response = session.get(url=URL)
print(response.status_code)
data = json.dumps(response.json(), indent=2)
print(data[:50])


# POST Request
with open(r'F:\IotIot\Resources\credentials.txt' , 'r') as file:
    credentials = json.load(file)

auth = HTTPBasicAuth(username=credentials['username'], password=credentials['password'])
content = {
    "title": "Post by Sarvesh",
    "content": "Rest API using Python",
    "status": "publish"
}
URL = "https://beelinkdirect.com/wp-json/wp/v2/posts/"
response = session.post(url=URL, auth=auth, json=content)
print(response.status_code)
data = json.dumps(response.json(), indent=2)
print(data[:50])


# Patch/ Update Request
URL = URL + str(response.json()["id"])
content = {
    "content": "This is the updated content through Python"
}
response = session.patch(url=URL, auth=auth, json=content)
print(response.status_code)


# Delete Request
URL = URL + "?force=true"
response = session.delete(url=URL, auth=auth)
print(response.status_code)

session.close()
