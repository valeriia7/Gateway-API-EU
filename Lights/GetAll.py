import requests

url = "https://192.168.8.100:443/v1/lights"

payload = {}
headers = {
  'Authorization': 'Bearer passcode=9E91380B1C063260AB6E56B5F75391BD jwt=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2Nsb3VkLmxlZHZhbmNlLmNvbS9zbWFydC1wcm9mZXNzaW9uYWwvYXBpLzEiLCJzdWIiOiI2MzkxYmUwNi1jNTdkLTRlMWQtOTVkMS1jMDE2NjJlZmJkOTAiLCJhdWQiOiJwcm9qZWN0OjQyMmRmMmMyLWQxMjUtNDg1OS05YzVkLTlmOTQ5ZGYwYTEzNSIsImV4cCI6MTU5ODAxODI3NCwiaWF0IjoxNTk4MDExMDczfQ.qbe1r4TW3jXHe9UAdlZ2OLvNzgG4nm7EKqAfHj-SqY3w74O5PwzgQ8nwk3Y-RUyKsv6LBJDpNKdPZm9egZJsUA'}

response = requests.request("GET", url, headers=headers, data = payload,cert=('..\\client.crt', '..\\client.pem.txt'),verify=False)

print(response.text.encode('utf8'))