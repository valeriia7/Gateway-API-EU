import requests
import sys
import os

import self as self


def override_where():
    """ overrides certifi.core.where to return actual location of cacert.pem"""
    # change this to match the location of cacert.pem
    return os.path.abspath("cacert.pem")


# is the program compiled?
if hasattr(sys, "frozen"):
    import certifi.core

    os.environ["REQUESTS_CA_BUNDLE"] = override_where()
    certifi.core.where = override_where

    # delay importing until after where() has been replaced
    import requests.utils
    import requests.adapters

    # replace these variables in case these modules were
    # imported before we replaced certifi.core.where
    requests.utils.DEFAULT_CA_BUNDLE_PATH = override_where()
    requests.adapters.DEFAULT_CA_BUNDLE_PATH = override_where()

url = "https://192.168.8.100:443/v1/gateways"

body = {}
headers = dict(Authorization='Bearer passcode=9E91380B1C063260AB6E56B5F75391BD '
                             'jwt=eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9'
                             '.eyJpc3MiOiJodHRwczovL2Nsb3VkLmxlZHZhbmNlLmNvbS9zbWFydC1wcm9mZXNzaW9uYWwvYXBpLzEiLCJzdWIiOiI2MzkxYmUwNi1jNTdkLTRlMWQtOTVkMS1jMDE2NjJlZmJkOTAiLCJhdWQiOiJwcm9qZWN0OjQyMmRmMmMyLWQxMjUtNDg1OS05YzVkLTlmOTQ5ZGYwYTEzNSIsImV4cCI6MTU5Nzc0Mzg1NCwiaWF0IjoxNTk3NzM2NjU0fQ.hxfVj-4UfYQIvryYJwSlBWGCh65vjbYd4M7EDZonBydrP3_FyI5XbImxDIK3Yn9sLXpu9LiBT1Y1nVBHTiEeNg ')

response = requests.get(url, headers=headers, data=body, verify='False')

print(response.text.encode('utf8'))
