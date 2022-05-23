from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
import schedule
from schedule import every, repeat
import functools
from functools import partial
from src.email_v2 import email_send
import time
from time import sleep
from crontab import CronTab


sched = BackgroundScheduler(daemon=True)
sched.start()
cron = CronTab(user='root')

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
            print(receiver)
            while True:
                 sleep(86400)
                 my_job(receiver)
                
                
            schedule.every(2).minutes.do(my_job, data['receiver'])
            #schedule.evert().minutes.do(my_job(receiver))
            #schedule.every().day.at("9:00").do(my_job)
            
        if data['period'] == 'e-week':
            while True:
                 sleep(86400)
                 my_job(receiver)
            # schedule.every(1).weeks.do(my_job)
            
        if data['period'] == 'e-fortnight':
            # schedule.every(2).weeks.do(my_job)
            
        if data['period'] == 'e-month':
            schedule.every(1).months.do(my_job)
            
        if data['period'] == 'e-year':  
            schedule.every(12).months.do(my_job)
    
    
    