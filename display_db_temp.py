import sqlite3
from sense_hat import SenseHat

dbname='assignmentone.db'

def displayData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM ASSIGNMENTONE_data"):
        print (row)
    conn.close()

# main function
def main():
	displayData()

# Execute program 
main()
