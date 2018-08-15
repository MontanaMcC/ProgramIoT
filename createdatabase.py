import sqlite3 as lite
import sys
con = lite.connect('assignmentone.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS ASSIGNMENTONE_data")
    cur.execute("CREATE TABLE ASSIGNMENTONE_data(temp NUMERIC, humidity NUMERIC)")
