#!/usr/bin/env python3
from crontab import CronTab
    
#init cron
cron = CronTab(user='pi')
cron.remove_all()

#add write_to_db cron and temp_notify cron
writejob = cron.new(command='/home/pi/Assignment_One/write_to_db.py')
notifyjob = cron.new(command='/home/pi/Assignment_One/temp_notify.py')
greetingjob = cron.new(command='/home/pi/Assignment_One/greeting.py')

#job settings
writejob.minute.every(59)
writejob.enable()
notifyjob.minute.every(59)
notifyjob.enable()
greetingjob.minute.every(59)
greetingjob.enable()
cron.write()
