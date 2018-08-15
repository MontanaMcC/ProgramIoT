import sqlite3
from sense_hat import SenseHat

dbname='assignmentone.db'

# get data from SenseHat sensor
def getSenseHatData():	
    sense = SenseHat()

    temp = sense.get_temperature()
    t = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    cputemp = t.read()
    cputemp = cputemp.replace('temp=','')
    cputemp = cputemp.replace('\'C\n','')
    cputemp = float(cputemp)
    newtemp = temp - ((cputemp - temp) / 2)

    humidity = sense.get_humidity()

    if newtemp is not None and humidity is not None:
        temp = round(newtemp, 1)
        humidity = round(humidity, 1)
        logData (newtemp, humidity)

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
