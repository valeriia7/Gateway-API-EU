import requests
from key import *
import json
url = "https://192.168.8.100:443/v1/lights/9480a509-20df-4bcb-81f2-d9cd664b64f5"
url2 = "https://192.168.8.100:443/v1/sensors/28dde6a9-4b86-45fc-b122-164516a616c6"
headers = {
         'Authorization': acctoken,
         'Content-Type': 'application/json'
     }
def cct(cct_value):
 payload = "{\n    \"cct\": " + str(cct_value) + " \n}"
 headers = {
  'Authorization': acctoken,
  'Content-Type': 'application/json'
}

 response = requests.request("PUT", url, headers=headers, data = payload,cert=('..\\cert\\client.crt', '..\\cert\\client.pem.txt'),verify=False)

 print(response.text.encode('utf8'))

def dim(dim_value):
     payload = "{\n    \"level\":" + str(dim_value) + " 10\n}"
     headers = {
         'Authorization': acctoken,
         'Content-Type': 'application/json'
     }

     response = requests.request("PUT", url, headers=headers, data=payload,
                                cert=('..\\cert\\client.crt', '..\\cert\\client.pem.txt'), verify=False)

     print(response.text.encode('utf8'))

def getSensorLight():
 payload  = {}
 headers = {
  'Authorization': acctoken}
 response = requests.request("GET", url2, headers=headers, data = payload,cert=('..\\cert\\client.crt', '..\\cert\\client.pem.txt'),verify=False)
 data = json.loads(response.text)
 light_level = data['obj']['light']
 return light_level