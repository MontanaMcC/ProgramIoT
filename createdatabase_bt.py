import sqlite3 as lite
import sys
con = lite.connect('assignmentonebt.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS ASSIGNMENTONEBT_data")
    cur.execute("CREATE TABLE ASSIGNMENTONEBT_data(name TEXT, address TEXT)")
