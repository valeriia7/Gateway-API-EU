import requests
from key import *
url = "https://192.168.8.100:443/v1/sensors/28dde6a9-4b86-45fc-b122-164516a616c6"

payload = "{\n    \"name\": \"test sensor\"\n}"
headers = {
  'Authorization': acctoken,
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data = payload,cert=('..\\client.crt', '..\\client.pem.txt'), verify = False)

print(response.text.encode('utf8'))
