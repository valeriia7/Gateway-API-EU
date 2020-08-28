import threading
import time

# f = open('config.ini', 'r')
# f.readlines()

a = []
def lightMeasurement():
 for cct in range (2700,6700,400):
     for dim in range(0,110,10):
      #time.sleep(1)
      a.append((cct,dim))

 return a




# def lightMeasurement():
#  for dim in range(0,110,10):
#       print(dim)
#       time.sleep(1)
#       a.append(dim)
#
#  return a

print(lightMeasurement())
