import configparser as cfp
config = cfp.ConfigParser()
config.sections()

config.read('config.ini')
CodeUsername = config['DEFAULT']['username']
CodePassword = config['DEFAULT']['password']
CodeProjectID = config['DEFAULT']['projectUuid']
CodeSensorsName = config['DEFAULT']['sensorsName']
CodeTimeValue = config['DEFAULT']['timeValue']


with open('config.ini','w') as configfile:
      config.write(configfile)





