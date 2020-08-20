import http.client
import mimetypes
conn = http.client.HTTPSConnection("staging-lsc-api.mondriaan.com")
payload = "{\r\n  \"accessToken\": \"eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2Nsb3VkLmxlZHZhbmNlLmNvbS9zbWFydC1wcm9mZXNzaW9uYWwvYXBpLzEiLCJzdWIiOiI2MzkxYmUwNi1jNTdkLTRlMWQtOTVkMS1jMDE2NjJlZmJkOTAiLCJhdWQiOiJwcm9qZWN0OjQyMmRmMmMyLWQxMjUtNDg1OS05YzVkLTlmOTQ5ZGYwYTEzNSIsImV4cCI6MTU5NzQyNTk3NSwiaWF0IjoxNTk3NDE4Nzc1fQ.KEA9DIoNUnLqALuObgHF3JnJJHzyNjVqVFAxy-QIMB7WFEfTaKY3MSis_etZh9cJvF7GTgwwwTcWrWXslzgsgg\"\r\n}\r\n"
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2Nsb3VkLmxlZHZhbmNlLmNvbS9zbWFydC1wcm9mZXNzaW9uYWwvYXBpLzEiLCJzdWIiOiI2MzkxYmUwNi1jNTdkLTRlMWQtOTVkMS1jMDE2NjJlZmJkOTAiLCJhdWQiOiJjbG91ZC1zZXJ2aWNlIiwiZXhwIjoxNTk4NTI3NzA0LCJpYXQiOjE1OTc2NjM3MDR9.mb-FicEyCR8_DiBA8xsEHM1HlsIrWF7nO9WHZNWQ8FhdSc2ygW7JXg3BT4yQUU9pfIhtvOZD3074NoND1yxf3A',
  'Content-Type': 'application/json'
}
conn.request("POST", "/api/1/projects/422df2c2-d125-4859-9c5d-9f949df0a135/lock", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))