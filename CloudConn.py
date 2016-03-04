#!/usr/bin/python
__author__ = 'mou'
from subprocess import call, check_output


def upload(SOURCE,DESTINATION):
    call(["scp", "-i", "/home/pi/Downloads/AWS_Service_Key.pem", SOURCE, "ubuntu@www.moutaigua.com:" + DESTINATION])

def delete(TARGET):
    call(["ssh", "-i", "/home/pi/Downloads/AWS_Service_Key.pem", "ubuntu@www.moutaigua.com", "rm " + TARGET])

def getRaspberryIp(KEYFILE):
    ip = check_output(["ssh", "-i", KEYFILE, "ubuntu@www.moutaigua.com", "cat /tmp/raspberryIP.txt"])
    return ip

