import requests
import json
import pdfkit
from pdfkit.api import configuration
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from src.error import AccessError

def email_send(send_to):
    url = "https://api.newrelic.com/graphql"

    payload = json.dumps({
    "query": "mutation {\n dashboardCreateSnapshotUrl(guid:\"MjkzNzIwMXxWSVp8REFTSEJPQVJEfDMwNDYyMDY\")\n}\n",
    "variables": ""
    })
    headers = {
    'Content-Type': 'application/json',
    'API-Key': 'NRAK-SO30FQVC7EL8X36VAOYQGAH8ZO4'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    data = json.loads(response.text)["data"]["dashboardCreateSnapshotUrl"]
    
    send_from = "seng2021icecream@gmail.com"
    password = "seng2021"   
    
    msg = MIMEMultipart()
    msg['Subject'] = '[Email Test]'
    msg['From'] = send_from
    msg['To'] = send_to

    # Attach body message to email
    msgText = MIMEText('<b>%s</b>' % ("Hello"), 'html')
    msg.attach(msgText)
    
    # Attach pdf
        # pdf = MIMEApplication(open(data, 'rb').read())
        # pdf.add_header('Content-Disposition',f'attachment;filename = data')
        # msg.attach(pdf) 

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            print("Starting server")
            smtpObj.login(send_from, password)
            print("Logged in")
            smtpObj.sendmail(send_from, send_to, msg.as_string())
            print("Done")
            
        return
    # If login fails or errors to server
    except Exception as e:
        raise AccessError(e)
