import requests
import json
import urllib
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
    
    response = urllib.request.urlopen(data)    
    file = open("dashboard" + ".pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Create file")
    
    send_from = "vinhhao.truong.004@gmail.com"
    password = "yugqjeuwluogdygr"  
    
    msg = MIMEMultipart()
    msg['Subject'] = 'New Relic Dashboard!'
    msg['From'] = send_from
    msg['To'] = send_to

    # Attach body message to email
    msgText = MIMEText('<b>%s</b>' % ("Hello! As requested, here is your current New Relic Dashboard :)"), 'html')
    msg.attach(msgText)
    
    try:
        with open('dashboard.pdf', "rb") as f:
                attach = MIMEApplication(f.read(),_subtype="pdf")
        attach.add_header('Content-Disposition','attachment',filename=str('dashboard.pdf'))
        msg.attach(attach)
        
    except Exception as e:
        raise AccessError(e)
        
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            print("Starting server")
            smtpObj.login(send_from, password)
            print("Logged in")
            print(send_to)
            smtpObj.sendmail(send_from, send_to, msg.as_string())
            print("Done")
            
        return
    # If login fails or errors to server
    except Exception as e:
        raise AccessError(e)
