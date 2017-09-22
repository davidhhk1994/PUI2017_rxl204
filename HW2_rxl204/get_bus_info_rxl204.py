
from __future__ import print_function
import pylab as pl
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

#Read MTA API

if not len(sys.argv) == 4:
	print ("Invalid number of arguments. Run as: python show_bus_locations_rxl204.py <MTA_KEY> <BUS_LINE> <BUS_LINE>")
	sys.exit()
#url = http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=25197ab7-fe61-4853-855e-f68a32e1e13b&VehicleMonitoringDetailLevel=calls&LineRef=B52

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=" + sys.argv[1] + "&VehicleMonitoringDetailLevel=calls&LineRef=" + sys.argv[2]

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

#Opens a file for writing
fout = open(sys.argv[2],"w")
fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

Bus_Count = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])

for i in (range(0,Bus_Count)):
	Bus_Lat = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	Bus_Long = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	Stop_Name = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
	Stop_Status = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'] 

	fout.write("%s,%s,%s,%s\n" %(Bus_Lat, Bus_Long, Stop_Name, Stop_Status))

