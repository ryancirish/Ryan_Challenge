#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime


remoteServerIP  = socket.gethostbyname('ryanc.irish')

print("scanning ryanc.irish")

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}:      Open".format(port))
        sock.close()

except socket.error:
    print("cant connect")
    sys.exit()


print('Scan complete')
