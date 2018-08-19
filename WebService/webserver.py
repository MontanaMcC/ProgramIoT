#!/usr/bin/env python3
import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request
from sense_hat import SenseHat

app = Flask(__name__)
db = '/home/pi/Assignment_One/assignmentone.db'
'''Uncomment if you dont want to see console print out'''
#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

def getData():
	conn = sqlite3.connect(db)
	curs = conn.cursor()
	temp = []
	hum = []
	for row in curs.execute("SELECT temp FROM ASSIGNMENTONE_data ORDER BY temp DESC LIMIT 10"):
		data = float(row[0])
		temp.append(data)
	for row in curs.execute("SELECT humidity FROM ASSIGNMENTONE_data ORDER BY humidity DESC LIMIT 10"):
		data = float(row[0])
		hum.append(data)
	conn.close()
	return temp, hum

# main route 
@app.route("/")
def index():	
	temp, hum = getData()
	templateData = {
		'temp': temp,
		'hum': hum,
	}
	return render_template('index.html', **templateData)

if __name__ == "__main__":
	host = os.popen('hostname -I').read()
	app.run(host=host, port=80, debug=False)
