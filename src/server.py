import os
from json import dumps
from flask import Flask, request, send_from_directory, render_template
from flask_cors import CORS
from src import config
from sqlalchemy import true
import requests
from src.log import take_log

from src.emails import send_email

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
 
 
@APP.route("/email/v1", methods=['GET'])
def email_send():
    APP.logger.info('------------ EMAIL ROUTE CALLED ------------')
    take_log()
    send_to = str(request.args.get('send_to'))
    print("Email Sending API In Progress...")
    return dumps(send_email(send_to))

    

if __name__ == "__main__":
    APP.run(port=config.PORT, debug=true, host="127.0.0.1")
    
