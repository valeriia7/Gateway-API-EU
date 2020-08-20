import requests

url = "https://staging-lsc-api.mondriaan.com/api/1/projects"

payload = {}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2Nsb3VkLmxlZHZhbmNlLmNvbS9zbWFydC1wcm9mZXNzaW9uYWwvYXBpLzEiLCJzdWIiOiI2MzkxYmUwNi1jNTdkLTRlMWQtOTVkMS1jMDE2NjJlZmJkOTAiLCJhdWQiOiJjbG91ZC1zZXJ2aWNlIiwiZXhwIjoxNTk4NTI3NzA0LCJpYXQiOjE1OTc2NjM3MDR9.mb-FicEyCR8_DiBA8xsEHM1HlsIrWF7nO9WHZNWQ8FhdSc2ygW7JXg3BT4yQUU9pfIhtvOZD3074NoND1yxf3A',
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
