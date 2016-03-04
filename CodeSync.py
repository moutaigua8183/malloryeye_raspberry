# used during development on my Mac

__author__ = 'mou'
from subprocess import call
from CloudConn import getRaspberryIp


def sync(project):
    if ( project == "malloryeye_aws"):
        call(["ssh", "-i", "/Users/mou/Dropbox/SSH/AWS_Service_Key.pem", "ubuntu@www.moutaigua.com",
              "cd /var/www/; "
              "git clone https://github.com/moutaigua8183/personal-webpage.git && "
              "cp -r -u personal-webpage/malloryeye/ html/; "
              "chmod 0740 html/malloryeye/*; "
              "rm -R -f personal-webpage;"])
    elif ( project == "malloryeye_raspberry" ):
        ip = getRaspberryIp()
        call(["ssh", "-i", "/Users/mou/Dropbox/SSH/AWS_Service_Key.pem", "ubuntu@" + ip,
              "cd /home/pi/Project/; "
              "rm -R -f malloryeye_raspberry; "
              "git clone https://github.com/moutaigua8183/malloryeye_raspberry.git; "
              "chmod -R 0740 malloryeye_raspberry; "])
    return
