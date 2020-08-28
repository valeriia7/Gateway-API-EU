import requests
from key import *
url = "https://192.168.8.100:443/v1/gateways/1/logs"

payload = {}
headers = {
  'Authorization': acctoken}

response = requests.request("GET", url, headers=headers, data = payload,cert=('..\\cert\\client.crt', '..\\cert\\client.pem.txt'), verify=False)

print(response.text.encode('utf8'))