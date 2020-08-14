import requests
# Get all gateways informations


url = "https://192.168.8.100:443/v1/gateways"

body = {}
headers = {
  'Authorization': 'Bearer passcode=9E91380B1C063260AB6E56B5F75391BD jwt=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2Nsb3VkLmxlZHZhbmNlLmNvbS9zbWFydC1wcm9mZXNzaW9uYWwvYXBpLzEiLCJzdWIiOiI2MzkxYmUwNi1jNTdkLTRlMWQtOTVkMS1jMDE2NjJlZmJkOTAiLCJhdWQiOiJjbG91ZC1zZXJ2aWNlIiwiZXhwIjoxNTk4MjcyOTY5LCJpYXQiOjE1OTc0MDg5Njl9.jSGfXiXQMOP3f2TJ1Nt3_HFwmjVm4_Jgc21-gdfr1nNvefzT-3YdXS3pmH3WeVfRmz1ONEtWETrQBlUhCFwQcw',
  '': ''
}

response = requests.get(url, headers=headers, data=body)

print(response.text.encode('utf8'))
