import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
from src.email_v2 import email_send
from datetime import date
from apscheduler.triggers.combining import AndTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
import time

sched = BackgroundScheduler(daemon=True)
sched.start()

def my_job(send_to):
    print("Doing Job...")
    email_send(send_to)
    print("Job Done!")
    
def scheduled(data):
    receiver = str(data['receiver'])
    if data['repeated'] == False:
        spec_date = data['date']
        time = spec_date.split("-")
        year = int(time[0])
        month = int(time[1])
        day = int (time[2])
        exec_date = date(year, month, day)
        
        print("Adding job...")
        ob = sched.add_job(my_job, 'date', run_date='2022-05-22 16:21:05', args = [receiver])
        print("Job added")

    if data['repeated'] == True:
        print(data['period'])
        if data['period'] == 'e-day':
            sched.add_job(my_job, 'interval', days=1, args=[receiver])
            
        if data['period'] == 'e-week':
            print(data['date'])
            day = str(data['date'])
            days = day[0:3]
            print (days)
            sched.add_job(my_job, 'cron', day_of_week= str(days),args=[receiver])
            
        if data['period'] == 'e-fortnight':
            day = data['date']
            days = day[0:3]
            print(days)
            
            sched.add_job(my_job, 'cron', day= '1st ' + days + ' 3rd ' + days, args=[receiver])
            
        if data['period'] == 'e-month':
            today = date.today()
            start = str(data['date'])
            year = str(today.year)
            month = str(today.month)
            start = year + "-" + month + "-" + start + " 23:18:00"
            print(start)
            sched.add_job(my_job, 'interval', weeks=4, start_date=str(start), args=[receiver])
            
        if data['period'] == 'e-year': 
            start = str(data['date'])
            print (start)
            start = start + "23:23:00"
            sched.add_job(my_job, 'interval', weeks=52, start_date=str(start), args=[receiver])
            
            
        
    