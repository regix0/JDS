from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
import schedule
from src.email_v2 import email_send

sched = BackgroundScheduler(daemon=True)
sched.start()

def job(data):
    send_to = data['receiver']
    email_send(send_to)

def scheduled(data):
    if data['repeated'] == False:
        spec_date = data['date']
        commas = data.replace("-", ",")
        exec_date = date(commas)
        ob = sched.add_date_job(job, exec_date, ['data'])

    if data['repeated'] == True:
        if data['period'] == 'e-day':
            schedule.every().day.at("9:00").do(job)
            
        if data['period'] == 'e-week':
            schedule.every(1).weeks.do(job)
            
        if data['period'] == 'e-fortnight':
            schedule.every(2).weeks.do(job)
            
        if data['period'] == 'e-month':
            schedule.every(1).months.do(job)
            
        if data['period'] == 'e-year':
            schedule.every(12).months.do(job)
    
    
    