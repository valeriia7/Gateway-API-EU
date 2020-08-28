import requests
from key import *
url = "https://192.168.8.100:443/v1/lights/9480a509-20df-4bcb-81f2-d9cd664b64f5"

payload = "{\n    \"rgb\": \"000080\"\n\n}"
headers = {
  'Authorization': acctoken,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data = payload,cert=('..\\cert\\client.crt', '..\\cert\\client.pem.txt'),verify=False)

print(response.text.encode('utf8'))