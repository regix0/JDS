import os
from json import dumps
from flask import Flask, request, send_from_directory, render_template, url_for, redirect
from flask_cors import CORS
from src import config
from sqlalchemy import true
import requests
from src.logging import take_log
from src.scheduling import scheduled
app = Flask(__name__)

from src.email_v2 import email_send

APP = Flask(__name__, template_folder='../templates')
CORS(APP)

def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response


APP.config['TRAP_HTTP_EXCEPTIONS'] = True
APP.register_error_handler(Exception, defaultHandler)
 
 
# @APP.route("/email/v2", methods=['GET'])
# def emails_send():
#     APP.logger.info('------------ EMAIL ROUTE CALLED ------------')
#     take_log()
#     send_to = str(request.args.get('send_to'))
#     print("Email Sending API In Progress...")
#     return dumps(email_send(send_to))

    
data = {
   'receiver': '',
   'repeated': False
}

@APP.route("/")
def home():
    APP.logger.info('------------ PAGE OPENED ------------')
    take_log()
    return render_template("index.html")

@APP.route("/onetime-form", methods=['GET', 'POST'])
def onetime_form():
   res = request.form
   APP.logger.info('------------ ONE TIME FORM CALLED ------------')
   take_log()
   #get data when is a response
   if (res):
      data.update({
         'receiver': res.get('receiver'),
         'repeated': False,
         'date': res.get('date')
      })
      scheduled(data)
   print(data)
   return render_template("single-form.html")

@APP.route("/repeated-form", methods=['GET', 'POST'])
def repeated_form():
   res = request.form
   APP.logger.info('------------ REPEATED FORM CALLED ------------')
   take_log()
   #get data when is a response
   if (res):
      data.update({
         'receiver': res.get('receiver'),
         'repeated': True,
         'period': res.get('period'),
      })
      #condition when there is a specific date
      if (res.get('date')):
         print(res.get('date'))
         data.update({
            'date' : res.get('date')
         })
      elif (data.get('date')): #when no date specified but there is a date in prev state
         data.pop('date') #remove prev date
      print(data)
      scheduled(data)  
   print(data)
   return render_template("repeated-form.html")
   
   
if __name__ == "__main__":
    APP.run(port=config.PORT, debug=true, host="127.0.0.1")
   
   # use_reloader=False
#  data usages:
#     ['receiver']: receiver email ->String
#     ['repeated']: False if one-time, True if repeated ->Bool
#     ['date']: ->String
#        - Specific date (One-time)
#        - Scheduling dates (Repeated)
#           + 'monday' to 'sunday' for every week and fortnight
#           + '1' to '31' for every month (have to use int() if needed)
#           + Specific date (like one-time) for every year
#     ['period']: (Repeated ONLY) ->String
#        - e-day: everyday
#        - e-month: every month
#        - e-fortnight: every fortnight
#        - e-week: every week
#        - e-year: every year
#  **NOTE** Try to run the main.py before merging to the project.