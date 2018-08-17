#!/usr/bin/env python3
import sqlite3
import os
import bluetooth
from sense_hat import SenseHat

sense = SenseHat()

temp = sense.get_temperature()
t = os.popen('/opt/vc/bin/vcgencmd measure_temp')
cputemp = t.read()
cputemp = cputemp.replace('temp=','')
cputemp = cputemp.replace('\'C\n','')
cputemp = float(cputemp)
newtemp = int(temp - ((cputemp - temp) / 2))

dbname='assignmentonebt.db'

def displayMessage():
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	nearby_devices = bluetooth.discover_devices()
	
	for mac_address in nearby_devices:
		for row in curs.execute("SELECT address FROM ASSIGNMENTONEBT_data WHERE address = (?)", (mac_address,)):
			address = row
			for row in curs.execute("SELECT name FROM ASSIGNMENTONEBT_data WHERE address = (?)", (address),):
				name = row
				sense.show_message("Hello {}. It is currently {} degrees".format(name, newtemp))			
	conn.close()

# main function
def main():
	displayMessage()

# Execute program 
main()
