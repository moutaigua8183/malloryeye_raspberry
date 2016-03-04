#!/usr/bin/python
# /etc/init.d/malloryeye_updateIP.py

#__author__ = 'mou'


from subprocess import call
import socket



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("gmail.com",80))
finally:
    ip = s.getsockname()[0]
s.close()
call(["echo", ip, ">", "/home/pi/Project/malloryeye_raspberry/raspberryIP.txt"]);
call(["scp", "-i", "/home/pi/Downloads/AWS_Service_Key.pem",
      "/home/pi/Project/malloryeye_raspberry/raspberryIP.txt",
      "ubuntu@www.moutaigua.com:/tmp/raspberryIP.txt"])
call(["rm", "/home/pi/Project/malloryeye_raspberry/raspberryIP.txt"]);