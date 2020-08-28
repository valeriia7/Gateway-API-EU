import requests
from key import *
import json
url = "https://192.168.8.100:443/v1/sensors"
arr  = []
payload = {}
headers = {
  'Authorization': acctoken}
response = requests.request("GET", url, headers=headers, data = payload,cert=('..\\cert\\client.crt', '..\\cert\\client.pem.txt'),verify=False)

data = json.loads(response.text)

light_level = data['obj']['light']
print(type(light_level))
