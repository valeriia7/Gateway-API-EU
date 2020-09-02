## Get acctoken
#  projectUuid was used from confi.py
import requests
from key import *
from config.config import *
url = "https://staging-lsc-api.mondriaan.com/api/1/projects/{0}".format(projectUuid)+"/lock"
print(url)
payload = "{\r\n  \"lockTTLInMinutes\": 120\r\n}\r\n"
headers = {
  'Authorization': token,
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
