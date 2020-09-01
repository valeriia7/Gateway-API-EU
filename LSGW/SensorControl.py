import time
import pandas as pd
from LSGW.RequestsSensorsLight import *
from config.config import *
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%d_%m_%Y_%H_%M_%S")
arr = []
for cct_value in range (2700,6700,400):
    str(cct(cct_value))
    print(cct_value)
    for dim_value in range(0,110,10):
      str(dim(dim_value))
      print(dim_value)
      time.sleep(timeValue)
      getSensorLight()
      arr.append((cct_value,dim_value,getSensorLight()))
      print(arr)
      csv = pd.DataFrame(arr).to_csv(sensorsName+'_report_' + current_time + '.csv')

