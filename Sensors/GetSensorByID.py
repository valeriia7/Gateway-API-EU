import requests
from key import *
url = "https://192.168.8.100:443/v1/sensors/28dde6a9-4b86-45fc-b122-164516a616c6"

payload  = {}
headers = {
  'Authorization': acctoken}
response = requests.request("GET", url, headers=headers, cert=('..\\cert\\client.crt', '..\\cert\\client.pem.txt'),verify=False)
