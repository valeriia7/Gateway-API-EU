# Gateway-API-EU

## How to start

* 1. Connect to WLAN(Ex.NB2) IP - http://192.168.8.100
* 2. Create account - https://staging-lsc-planningtool.mondriaan.com/login
-> add sensor and lamp
* 3. Add cert and cert.key to postmann 
* 4. Auth and get token https://staging-lsc-api.mondriaan.com/api/1/auth/login
* 5. Generate Accsestoken https://staging-lsc-api.mondriaan.com/api/1/projects/projectuuid/lock
* 6 Create key.py and add token from 3 and acctoken from 4 to var 
* 7. Add cert to python 



## The task is the following

1.	Decommission the bulb and the sensor from the ZigBee dongle 
2.	Give back the dongle 
3.	Set-up a mini Vivares system from the GW + router I left on your desk
4.	Connect to the cloud service and create a test config
* a.	1 room
* b.	1 bulb + 1 sensor (same types as you have now)
5.	Do the commissioning of the devices with the APP and keep them close to each other 
6.	Get the IP address of the GW from the menu of the Router
7.	Get an access token from the cloud service with Postman (valid for 24h!)
8.	Get the GW status with Postman
9.	Get the light level value of the sensor with Postman
10.	Switch on/off and the bulb with Postman
11.	Based on the experience you have gained during the previous points, write a tool in phyton:
* a.	Which is increasing the light level of the bulb with 10% in each step
* b.	Waits some sec until the light flux is stable and the sensor could measure it
* c.	Reads the measured light level value from the attached sensor
* d.	And repeats the point above until 100%
* e.	Finally it creates a table with the dim steps and the measured value
12.	The SW should
* a.	Have an architectural plan before the implementation
* b.	Stored in a local git repository
* c.	Commented with Doxygen compatible comments
* d.	Use a .conf file where the use can manually specify
** i.	The IP address of the GW
** ii.	The Vivares user name and Password
* e.	Be converted in its final form to an exe file which can independently run of windows machines

