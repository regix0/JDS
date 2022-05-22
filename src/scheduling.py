from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
import schedule
from src.email_v2 import email_send

sched = BackgroundScheduler(daemon=True)
sched.start()

def my_job(send_to):
    print("Doing Job...")
    email_send(send_to)
    print("Job Done!")

def scheduled(data):
    if data['repeated'] == False:
        spec_date = data['date']
        time = spec_date.split("-")
        year = int(time[0])
        month = int(time[1])
        day = int (time[2])
        exec_date = date(year, month, day)
        send_to = data['receiver']
        
        print("Adding job...")
        ob = sched.add_job(my_job, 'date', run_date='2022-05-22 13:24:05', args = ['send_to'])
        print("Job added")

    if data['repeated'] == True:
        if data['period'] == 'e-day':
            schedule.every().day.at("9:00").do(my_job)
            
        if data['period'] == 'e-week':
            schedule.every(1).weeks.do(my_job)
            
        if data['period'] == 'e-fortnight':
            schedule.every(2).weeks.do(my_job)
            
        if data['period'] == 'e-month':
            schedule.every(1).months.do(my_job)
            
        if data['period'] == 'e-year':
            schedule.every(12).months.do(my_job)
    
    
    