#!/usr/bin/python
__author__ = 'mou'
from subprocess import call, check_output


def upload(SOURCE,DESTINATION):
    call(["scp", "-i", "AWS_Service_Key.pem", SOURCE, "ubuntu@www.moutaigua.com:" + DESTINATION])

def delete(TARGET):
    call(["ssh", "-i", "AWS_Service_Key.pem", "ubuntu@www.moutaigua.com", "rm " + TARGET])

def getRaspberryIp():
    ip = check_output(["ssh", "-i", "AWS_Service_Key.pem", "ubuntu@www.moutaigua.com",
                                  "cat /tmp/raspberryIP.txt"])
    return ip

