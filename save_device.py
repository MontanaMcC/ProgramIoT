#!/usr/bin/env python3
import sqlite3
import bluetooth
import os
import time
from sense_hat import SenseHat

dbname='/home/pi/Assignment_One/assignmentonebt.db'

# Main function
def main():
	user_name = input("Enter your name: ")
	device_name = input("Enter the name of your phone: ")
	search(user_name, device_name)

# Logs the phone bt address to the name given
def logDevice (name, address):	
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	curs.execute("INSERT INTO ASSIGNMENTONEBT_data values(?, ?)", (name, address))
	conn.commit()
	conn.close()
	
# Search for device based on device's name
def search(user_name, device_name):
	while True:
		device_address = None
		dt = time.strftime("%a, %d %b %y %H:%M:%S", time.localtime())
		print("\nCurrently: {}".format(dt))
		time.sleep(3) #Sleep three seconds 
		nearby_devices = bluetooth.discover_devices()
	
		#if device is found, add to database
		for mac_address in nearby_devices:
			if device_name == bluetooth.lookup_name(mac_address, timeout=5):
				device_address = mac_address
				break
		if device_address is not None:
			print("Hi {}! Your phone ({}) has the MAC address: {}".format(user_name, device_name, device_address))
			logDevice(user_name, device_address)
			sense = SenseHat()
			sense.show_message("Device connected")
			break
		else:
			print("Could not find target device nearby...")

#Execute program
main()
