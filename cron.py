#!/usr/bin/env python3
from crontab import CronTab
    
#init cron
cron = CronTab(user='pi')
cron.remove_all()

#add write_to_db cron and temp_notify cron
writejob = cron.new(command='/home/pi/Assignment_One/write_to_db.py')
notifyjob = cron.new(command='/home/pi/Assignment_One/temp_notify.py')

#job settings
writejob.hour.every(1)
writejob.enable()
notifyjob.hour.every(1)
notifyjob.enable()
cron.write()
