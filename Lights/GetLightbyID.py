import requests
from key import *
url = "https://192.168.8.100:443/v1/lights/9480a509-20df-4bcb-81f2-d9cd664b64f5"

payload = {}
headers = {
  'Authorization': acctoken}
response = requests.request("GET", url, headers=headers, data = payload,cert=('..\\client.crt', '..\\client.pem.txt'),verify=False)
