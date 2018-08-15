#!/usr/bin/env python3
import requests
import json
import os
from sense_hat import SenseHat

sense = SenseHat()

temp = sense.get_temperature()
t = os.popen('/opt/vc/bin/vcgencmd measure_temp')
cputemp = t.read()
cputemp = cputemp.replace('temp=','')
cputemp = cputemp.replace('\'C\n','')
cputemp = float(cputemp)
newtemp = int(temp - ((cputemp - temp) / 2))

ACCESS_TOKEN="o.rp5PkdYhFkIjPEnQfGPSWsilUf2w2EM3"

def send_notification_via_pushbullet(title, body):
    """ Sending notification via pushbullet.
        Args:
            title (str) : title of text.
            body (str) : Body of text.
    """
    data_send = {"type": "note", "title": title, "body": body}
 
    resp = requests.post('https://api.pushbullet.com/v2/pushes', data=json.dumps(data_send),
                         headers={'Authorization': 'Bearer ' + ACCESS_TOKEN, 
                         'Content-Type': 'application/json'})
    if resp.status_code != 200:
        raise Exception('Something wrong')
    else:
        print('complete sending')

#main function
def main():
	print(newtemp)
	if newtemp < 20:
		send_notification_via_pushbullet("Bring a sweater, it's %d degrees!" % newtemp, "From Raspberry Pi")

#Execute
main()
