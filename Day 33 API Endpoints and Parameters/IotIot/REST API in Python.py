import requests
import json
from requests.auth import HTTPBasicAuth

# GET Request
session = requests.session()
URL = "https://beelinkdirect.com/wp-json/wp/v2/posts?_fields=id,title,content&page=1"
response = session.get(url=URL)
print(response.status_code)
data = json.dumps(response.json(), indent=2)
print(data)


# POST Request
auth = HTTPBasicAuth(username='aditya', password='qee9 NRfx 9LM4 3SZf IEkN EX3W')
content = {
    "title": "Post by Sarvesh",
    "content": "Rest API using Python",
    "status": "publish"
}
URL = "https://beelinkdirect.com/wp-json/wp/v2/posts/"
response = session.post(url=URL, auth=auth, json=content)
print(response.status_code)
data = json.dumps(response.json(), indent=2)
print(data)


# Patch/ Update Request
URL = URL + str(response.json()["id"])
content = {
    "content": "This is the updated content through Python"
}
response = session.patch(url=URL, auth=auth, json=content)
print(response.status_code)


# Delete Request
response = session.delete(url=URL, auth=auth)
print(response.status_code)

session.close()
