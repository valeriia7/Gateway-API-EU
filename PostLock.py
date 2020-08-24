import requests
from key import *
url = "https://staging-lsc-api.mondriaan.com/api/1/projects/422df2c2-d125-4859-9c5d-9f949df0a135/lock"

payload = "{\r\n  \"lockTTLInMinutes\": 120\r\n}\r\n"
headers = {
  'Authorization': token,
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))