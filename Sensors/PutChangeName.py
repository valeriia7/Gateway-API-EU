import requests

url = "https://192.168.8.100:443/v1/sensors/28dde6a9-4b86-45fc-b122-164516a616c6"

payload = "{\n    \"name\": \"test sensor\"\n}"
headers = {
  'Authorization': 'Bearer passcode=9E91380B1C063260AB6E56B5F75391BD jwt=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2Nsb3VkLmxlZHZhbmNlLmNvbS9zbWFydC1wcm9mZXNzaW9uYWwvYXBpLzEiLCJzdWIiOiI2MzkxYmUwNi1jNTdkLTRlMWQtOTVkMS1jMDE2NjJlZmJkOTAiLCJhdWQiOiJwcm9qZWN0OjQyMmRmMmMyLWQxMjUtNDg1OS05YzVkLTlmOTQ5ZGYwYTEzNSIsImV4cCI6MTU5ODAwOTIwOSwiaWF0IjoxNTk4MDAyMDA4fQ.qegCFaypz3i7ATBHIAS--yAxebmo8oc8KZqiwQkT7OHKX9mnHzT2GAgJ1AXmJSVjozgcJZH2WfL3HFphKg-ptA',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data = payload,cert=('..\\client.crt', '..\\client.pem.txt'), verify = False)

print(response.text.encode('utf8'))