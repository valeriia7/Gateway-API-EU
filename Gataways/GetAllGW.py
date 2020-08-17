import requests

url = "https://192.168.8.100:443/v1/gateways"

body = {}
headers = {
  'Authorization': 'Bearer passcode=9E91380B1C063260AB6E56B5F75391BD '
                   'jwt=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9'
                   '.eyJpc3MiOiJodHRwczovL2Nsb3VkLmxlZHZhbmNlLmNvbS9zbWFydC1wcm9mZXNzaW9uYWwvYXBpLzEiLCJzdWIiOiI2MzkxYmUwNi1jNTdkLTRlMWQtOTVkMS1jMDE2NjJlZmJkOTAiLCJhdWQiOiJwcm9qZWN0OjQyMmRmMmMyLWQxMjUtNDg1OS05YzVkLTlmOTQ5ZGYwYTEzNSIsImV4cCI6MTU5NzY3ODYyMiwiaWF0IjoxNTk3NjcxNDIyfQ.-d3Yx6ooOCuOcxkjKM0J_AUz-zUtSCSCuu-yC6JuPSXTmR9NaYybiH8HVuH-ZRrz93Yr3Qcx8HXQ3PZGzStEfg '
}

response = requests.get(url, headers=headers, data=body, verify=False)


print(response.text.encode('utf8'))
