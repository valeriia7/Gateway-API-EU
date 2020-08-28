import requests
import time
from key import *
import json
from test.testcsv import *
import pandas as pd
arr = []
url = "https://192.168.8.100:443/v1/lights/9480a509-20df-4bcb-81f2-d9cd664b64f5"
url2 = "https://192.168.8.100:443/v1/sensors/28dde6a9-4b86-45fc-b122-164516a616c6"
for cct_value in range (2700,6700,400):
    payload1 = "{\n    \"cct\": " + str(cct_value) + "\n}"
    print(payload1)
    headers = {
        'Authorization': acctoken,
        'Content-Type': 'application/json'
    }
    response = requests.request("PUT", url, headers=headers, data=payload1, cert=('..\\cert\\client.crt', '..\\cert\\client.pem.txt'),
                               verify=False)

    #arr.append(cct_value)
    for dim in range(0,110,10):
      payload =  "{\n\"level\": " + str(dim) + "\n}"
      #arr.append(dim)

      print(payload)


      headers = {
      'Authorization': acctoken,
      'Content-Type': 'application/json'
}

      response = requests.request("PUT", url, headers=headers, data = payload,cert=('..\\cert\\client.crt', '..\\cert\\client.pem.txt'),verify=False)
      time.sleep(5)

      body = {}
      hl = {
          'Authorization': acctoken}
      r = requests.request("GET", url2, headers=hl, data=body,
                                 cert=('..\\cert\\client.crt', '..\\cert\\client.pem.txt'), verify=False)
      data = json.loads(r.text)
      light_level =data['obj']['light']


      arr.append((cct_value,dim,light_level))

      print(response.text.encode('utf8'))
      print(arr)
      # timetable = {
      #     'cct': arr[0],
      #     'dim': arr[1],
      #     'light': arr[2]
      # }
      # df = pd.DataFrame(arr)
      csv = pd.DataFrame(arr).to_csv('VIVARES_ZB_LO_SENS_report_' + current_time + '.csv')
      # df.to_csv('sensor_report_FREETEXT_DATE_TIME.csv')
      #print(csv)

