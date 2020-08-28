import time
from testcase.testcsv import *
import pandas as pd
from LSGW.RequestsSensorsLight import *
arr = []
for cct_value in range (2700,6700,400):
    str(cct(cct_value))
    print(cct_value)
    for dim_value in range(0,110,10):
      str(dim(dim_value))
      print(dim_value)
      time.sleep(1)
      getSensorLight()
      arr.append((cct_value,dim_value,getSensorLight()))
      print(arr)
      csv = pd.DataFrame(arr).to_csv('VIVARES_ZB_LO_SENS_report_' + current_time + '.csv')

