#!/usr/bin/python
# /etc/init.d/malloryeye_updateIP.py

#__author__ = 'mou'


### BEGIN INIT INFO
# Provides:          malloryeye_updateIP.py
# Required-Start:   $all
# Required-Stop:
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start daemon at boot time
# Description:       Enable service provided by daemon.
### END INIT INFO

from subprocess import call
import socket
import os



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("gmail.com",80))
finally:
    ip = s.getsockname()[0]
s.close()
os.system(["echo " + ip + "> /home/pi/Project/malloryeye_raspberry/raspberryIP.txt"]);
call(["scp", "-i", "/home/pi/Downloads/AWS_Service_Key.pem",
      "/home/pi/Project/malloryeye_raspberry/raspberryIP.txt",
      "ubuntu@www.moutaigua.com:/tmp/raspberryIP.txt"])
call(["rm", "/home/pi/Project/malloryeye_raspberry/raspberryIP.txt"]);