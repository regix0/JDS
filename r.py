import requests
import json
import pdfkit
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

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

    pdfkit.from_url(data,'r.pdf')
    
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
    pdf = MIMEApplication(open('r.pdf', 'rb').read())
    pdf.add_header('Content-Disposition',f'attachment;filename = r.pdf')
    msg.attach(pdf) 

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(send_from, password)
            smtpObj.sendmail(send_from, send_to, msg.as_string())
            
    # If login fails or errors to server
    except Exception as e:
        print(e)