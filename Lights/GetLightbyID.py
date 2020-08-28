import requests
from key import *
import json
r = []
url = "https://192.168.8.100:443/v1/lights/9480a509-20df-4bcb-81f2-d9cd664b64f5"

payload = {}
headers = {
  'Authorization': acctoken}
response = requests.request("GET", url, headers=headers, data = payload,cert=('..\\cert\\client.crt', '..\\cert\\client.pem.txt'),verify=False)
data = json.loads(response.text)
print(data['obj'])
#r.append(data)
# namesList = []
# for s in data['obj']:
#     name = (s['cct'])
#     print(namesList.append(name))
