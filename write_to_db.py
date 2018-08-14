import time
import sqlite3
from sense_hat import SenseHat

dbname='assignmentone.db'
sampleFreq = 1 # time in seconds
setTime = time.ctime()

# get data from SenseHat sensor
def getSenseHatData():	
    sense = SenseHat()
    temp = sense.get_temperature()
    humidity = sense.get_humidity()

    if temp is not None and humidity is not None:
        temp = round(temp, 1)
        humidity = round(humidity, 1)
        logData (temp, humidity)

# log sensor data on database
def logData (temp, humidity):	
	conn=sqlite3.connect(dbname)
	curs=conn.cursor()
	curs.execute("INSERT INTO ASSIGNMENTONE_data values(?, ?, ?)", (setTime, temp, humidity))
	conn.commit()
	conn.close()

# display database data
def displayData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM ASSIGNMENTONE_data"):
        print (row)
    conn.close()

# main function
def main():
	while True:
		getSenseHatData()
		displayData()
		time.sleep(sampleFreq)

# Execute program 
main()
