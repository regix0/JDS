import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def send_email(send_to):
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
        
#def schedule_time(time_send):
    
