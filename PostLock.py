import requests

url = "https://staging-lsc-api.mondriaan.com/api/1/projects/422df2c2-d125-4859-9c5d-9f949df0a135/lock"

payload = "{\r\n  \"lockTTLInMinutes\": 120\r\n}\r\n"
headers = {
  'Authorization': 'Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2Nsb3VkLmxlZHZhbmNlLmNvbS9zbWFydC1wcm9mZXNzaW9uYWwvYXBpLzEiLCJzdWIiOiI2MzkxYmUwNi1jNTdkLTRlMWQtOTVkMS1jMDE2NjJlZmJkOTAiLCJhdWQiOiJjbG91ZC1zZXJ2aWNlIiwiZXhwIjoxNTk4ODY2NDUwLCJpYXQiOjE1OTgwMDI0NDl9.Q-HrZ5aPvM3_SnKGnK-HkW5bQ9Cdb98mAGEvlzimmSltWhE-ogucp2LAVsW0IqJzuLZfIiDxbSDecCPKZvyrhw',
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))