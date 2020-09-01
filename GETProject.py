import requests
from key import *
from config.config import *
print(username)
url = "https://staging-lsc-api.mondriaan.com/api/1/projects"

payload = {}
headers = {
  'Authorization': token,
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
