import sqlite3
from sense_hat import SenseHat

dbname='assignmentone.db'

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
	curs.execute("INSERT INTO ASSIGNMENTONE_data values(?, ?)", (temp, humidity))
	conn.commit()
	conn.close()

# main function
def main():
	getSenseHatData()

# Execute program 
main()
