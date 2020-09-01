import configparser as cfp
from pathlib import Path
config = cfp.ConfigParser()
config.sections()

config.read('config.ini')

username = config.get('DEFAULT','username')
password = config.get('DEFAULT','password')
projectUuid = config.get('DEFAULT','projectUuid')
sensorsName = config.get('DEFAULT','sensorsName')
timeValue = config.getint('DEFAULT','timeValue')


