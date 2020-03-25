#!/usr/bin/env

""" Cisco DNA Center - Interfaces Port Speed (custom) Reporting
Copyright (c) 2020 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.1 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

__author__ = "Yossi Meloch"
__email__ = "ymeloch@cisco.com"
__version__ = "0.1.0"
__copyright__ = "Copyright (c) 2020 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.1"


import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json
import sys
import os
import datetime
import getpass
import tabulate
import requests
from requests.auth import HTTPBasicAuth
import warnings
warnings.filterwarnings("ignore")
requests.packages.urllib3.disable_warnings()

os.system('clear')

print("DNA Center - Interface Speed Configuration")
print("------------------------------------------")
print
dnac_ip     = input('IP Address or Hostname: ')
username 	= input('Username: ')
password 	= getpass.getpass('Password: ')

def getToken():
    post_url = "https://" + dnac_ip + "/api/system/v1/auth/token"
    headers = {'content-type': 'application/json'}
    response = requests.post(post_url,
    auth=HTTPBasicAuth(username=username,password=password),
    headers=headers,verify=False)
    if response.status_code != 200:
        print ("Verify Login \t\t\t\t \033[1;31;40m FAIL \033[0;0m")
        sys.exit()
    print
    print ("Verify Login \t\t\t\t \033[1;32;40m PASS \033[0;0m")
    print ("Retrieve Token ID \t\t\t \033[1;32;40m PASS \033[0;0m")
    r_json=response.json()
    token = r_json["Token"]
    return token

def getInterfaceStatus(token):
    url = "https://" + dnac_ip + "/api/v1/interface"
    header = {"content-type": "application/json", "X-Auth-Token":token}
    response = requests.get(url, headers=header, verify=False)
    if response.status_code != 200:
        print ("Retrieve Interfaces Status \t\t \033[1;31;40m FAIL \033[0;0m")
        sys.exit()
    print ("Retrieve Interfaces Status \t\t \033[1;32;40m PASS \033[0;0m")
    r_json=response.json()
    devices = r_json["response"]
    device_list = []
    i=0
    for item in devices:
            i+=1
            device_list.append([i,item["portName"],item["portMode"],item["interfaceType"],item["status"],item["adminStatus"],item["speed"],item["vlanId"],item["ipv4Address"]])
    table = (tabulate.tabulate(device_list, headers=['Port Name','Port Mode','Interface Type','Oper Status', 'Admin Satus', 'Speed (Kbit/sec)', 'VLAN ID', 'IP Address'],tablefmt="fancy_grid", numalign="center"))
    return table

def tableFormat(table):
    print ("Formelizing Data \t\t\t \033[1;32;40m DONE \033[0;0m")
    print
    print(table)

theTicket = getToken()
thegetInterfaceStatus = getInterfaceStatus(theTicket)
thetableFormat = tableFormat(thegetInterfaceStatus)
