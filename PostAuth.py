import requests

url = "https://staging-lsc-api.mondriaan.com/api/1/auth/login"

body = "{\r\n  \"email\": \"V.Kulakova@ledvance.com\"," \
       "\r\n  \"password\": \"k1sH3rceG\"\r\n} "
headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data = body)

print(response.text.encode('utf8'))
