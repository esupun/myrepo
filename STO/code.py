#!/usr/local/bin/python3
 

from netmiko import ConnectHandler
import os
directory = os.getcwd()

conf = os.path.join(directory,input ("\n Name of Command File :-\n"))
hostfile = os.path.join(directory,input ("\n Name of Host File :-\n"))
username = 'supun'
password = 'Juniper!1'
platform = 'juniper_junos'
port = '22'

with open(hostfile) as f:
    for line in f:
        host = line.strip()
        try:
            print ("\nConnecting ")
      net_connect = ConnectHandler(device_type=platform, ip=host, username=username, password=password, port = port) 
      print ('\nConnected to {}, gathering info...\n'.format(host))

with open(conf) as f:
   for line in f:
      command=line.strip()
      try:
    print(command)
    output = net_connect.send_command(command)
    print(output)

      except:
          print("Error running {} command".format(command))

      except:
          print ('Error Connecting {}'.format(host)) 
