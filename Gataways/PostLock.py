import requests

url = "https://staging-lsc-api.mondriaan.com/api/1/projects/422df2c2-d125-4859-9c5d-9f949df0a135/lock"

body = "{\r\n  \"lockTTLInMinutes\": 120\r\n}\r\n"
headers = {
  'Authorization': 'Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2Nsb3VkLmxlZHZhbmNlLmNvbS9zbWFydC1wcm9mZXNzaW9uYWwvYXBpLzEiLCJzdWIiOiI2MzkxYmUwNi1jNTdkLTRlMWQtOTVkMS1jMDE2NjJlZmJkOTAiLCJhdWQiOiJjbG91ZC1zZXJ2aWNlIiwiZXhwIjoxNTk4MjgyMTkwLCJpYXQiOjE1OTc0MTgxODl9.WvBZ-QFc1SlFjORi6B2SGNXY0sYsDzyN6SgbfRU_a4LVARVoSWGPprObtLqqBwKnI_kxCk9e_2Vu06FMmWJvqw',
  'Accept': 'application/json',
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data = body)

print(response.text.encode('utf8'))
