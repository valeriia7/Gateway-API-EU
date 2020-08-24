import requests
from key import *
url = "https://192.168.8.100:443/v1/sensors"

payload = {}
headers = {
  'Authorization': acctoken}
response = requests.request("GET", url, headers=headers, data = payload,cert=('..\\client.crt', '..\\client.pem.txt'),verify=False)

print(response.text.encode('utf8'))