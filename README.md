# Cisco DNA Center - Interfaces Speed (custom) Report

Ever wondered how to create a custom Cisco DNA Center report?  <br /> For example, "Get all Interfaces Ports Speed" report?  <br /> <br />
As part of this tutorial/repository, you will learn how to leverage the "Get All Interfaces" API call do build a custom/tailor-made report. <br />
The generated data can be then uploaded/integrated with cross-solutions such as Spark, Qlik, SmartSheet, and others.  <br />

![alt text](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/story2.png) <br />

### Objectives and Flow
![alt text](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/lab2Flow.png)

## Description

1. Let us start with reviewing the available DNA Center "Interfaces" API calls in **[Cisco documentation](https://developer.cisco.com/site/dna-center-rest-api/)** (Hint: Search for ***"Get all interfaces"*** under the ***"Devices"*** submenu). <br />

2. Right-click on the following GET API call to get in-depth information about all the available data types. <br />
<p align="center">
    <a href="https://developer.cisco.com/site/dna-center-rest-api/"><img src="https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/newReport1.png" title="DNA Center API Calls" align="center" /></a>
</p>

3. Review the available data (i.e., response) of this API call. Do you see any value that may help with?

    ```yaml
    {
      "response": [
        {
          "adminStatus": "string",
          "className": "string",
          "description": "string",
          "deviceId": "string",
          "duplex": "string",
          "id": "string",
          "ifIndex": "string",
          "instanceTenantId": "string",
          "instanceUuid": "string",
          "interfaceType": "string",
          "ipv4Address": "string",
          "ipv4Mask": "string",
          "isisSupport": "string",
          "lastUpdated": "string",
          "macAddress": "string",
          "mappedPhysicalInterfaceId": "string",
          "mappedPhysicalInterfaceName": "string",
          "mediaType": "string",
          "nativeVlanId": "string",
          "ospfSupport": "string",
          "pid": "string",
          "portMode": "string",
          "portName": "string",
          "portType": "string",
          "serialNo": "string",
          "series": "string",
     =>   "speed": "string",  <=
          "status": "string",
          "vlanId": "string",
          "voiceVlan": "string"
        }
      ],
      "version": "string"
    }
    ```
**"speed": "string"**<br />
**Great Job, you have found it!** :thumbsup: <br /> <br />

4. So what's the next step? <br /> Let us create a simple Python script which leverage the Cisco DNA Center "Get all interfaces" API call to build our custom report! <br />

## Installation

### Repo Clone
5. Open a **Terminal** window (Press CMD + Space, type "Terminal" and hit return). <br />

6. Clone the code to your workstation (Copy & Paste the commands below). <br />

    ```concole
    cd /tmp
    git clone https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-.git
    cd dnac-InterfacePortSpeedReport-
    ```

### Lab Initialization
7. From the terminal window, run **`./setup.sh`** to initialize the lab environment. This will create a Python virtual environment, activate it, and install prerequisites. <br />

:warning:**Note: This step may take 1 - 2 minutes.**

<details>
          <summary>Sample Setup Output"</summary>

 ```concole
      Setting up the workstation environment for the lab.

      Creating Python 3 Virtual Environment
      Collecting requests (from -r requirements.txt (line 1))
        Using cached https://files.pythonhosted.org/packages/ff/17/5cbb026005115301a8fb2f9b0e3e8d32313142fe8b617070e7baad20554f/requests-2.20.1-py2.py3-none-any.whl
      Collecting pyOpenSSL (from -r requirements.txt (line 2))
        Using cached https://files.pythonhosted.org/packages/96/af/9d29e6bd40823061aea2e0574ccb2fcf72bfd6130ce53d32773ec375458c/pyOpenSSL-18.0.0-py2.py3-none-any.whl
      Collecting ndg-httpsclient (from -r requirements.txt (line 3))
        Using cached https://files.pythonhosted.org/packages/fb/67/c2f508c00ed2a6911541494504b7cac16fe0b0473912568df65fd1801132/ndg_httpsclient-0.5.1-py3-none-any.whl
      Collecting pyasn1 (from -r requirements.txt (line 4))
        Using cached https://files.pythonhosted.org/packages/d1/a1/7790cc85db38daa874f6a2e6308131b9953feb1367f2ae2d1123bb93a9f5/pyasn1-0.4.4-py2.py3-none-any.whl
      Collecting tabulate (from -r requirements.txt (line 5))
        Using cached https://files.pythonhosted.org/packages/12/c2/11d6845db5edf1295bc08b2f488cf5937806586afe42936c3f34c097ebdc/tabulate-0.8.2.tar.gz
      Collecting six (from -r requirements.txt (line 6))
        Using cached https://files.pythonhosted.org/packages/67/4b/141a581104b1f6397bfa78ac9d43d8ad29a7ca43ea90a2d863fe3056e86a/six-1.11.0-py2.py3-none-any.whl
      Collecting slackclient (from -r requirements.txt (line 7))
        Using cached https://files.pythonhosted.org/packages/0d/2f/1378e64a843a5a8a83d73caa59ac88c36c67e2b41ac0fab3422080ff13bd/slackclient-1.3.0-py2.py3-none-any.whl
      Collecting simple-crypt (from -r requirements.txt (line 8))
        Using cached https://files.pythonhosted.org/packages/60/66/5bf6feb073f715a61492f8a6d444ad3d884ada71af317ce7a9c80bebee60/simple-crypt-4.1.7.tar.gz
      Collecting idna<2.8,>=2.5 (from requests->-r requirements.txt (line 1))
        Using cached https://files.pythonhosted.org/packages/4b/2a/0276479a4b3caeb8a8c1af2f8e4355746a97fab05a372e4a2c6a6b876165/idna-2.7-py2.py3-none-any.whl
      Collecting urllib3<1.25,>=1.21.1 (from requests->-r requirements.txt (line 1))
        Using cached https://files.pythonhosted.org/packages/62/00/ee1d7de624db8ba7090d1226aebefab96a2c71cd5cfa7629d6ad3f61b79e/urllib3-1.24.1-py2.py3-none-any.whl
      Collecting certifi>=2017.4.17 (from requests->-r requirements.txt (line 1))
        Using cached https://files.pythonhosted.org/packages/56/9d/1d02dd80bc4cd955f98980f28c5ee2200e1209292d5f9e9cc8d030d18655/certifi-2018.10.15-py2.py3-none-any.whl
      Collecting chardet<3.1.0,>=3.0.2 (from requests->-r requirements.txt (line 1))
        Using cached https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl
      Collecting cryptography>=2.2.1 (from pyOpenSSL->-r requirements.txt (line 2))
        Using cached https://files.pythonhosted.org/packages/18/d5/7f725ac9ff162c93f67087414961b8256019527093d31e4c1fa9c377170a/cryptography-2.4.2-cp34-abi3-macosx_10_6_intel.whl
      Collecting websocket-client<1.0a0,>=0.35 (from slackclient->-r requirements.txt (line 7))
        Using cached https://files.pythonhosted.org/packages/26/2d/f749a5c82f6192d77ed061a38e02001afcba55fe8477336d26a950ab17ce/websocket_client-0.54.0-py2.py3-none-any.whl
      Collecting pycrypto (from simple-crypt->-r requirements.txt (line 8))
        Using cached https://files.pythonhosted.org/packages/60/db/645aa9af249f059cc3a368b118de33889219e0362141e75d4eaf6f80f163/pycrypto-2.6.1.tar.gz
      Collecting cffi!=1.11.3,>=1.7 (from cryptography>=2.2.1->pyOpenSSL->-r requirements.txt (line 2))
        Using cached https://files.pythonhosted.org/packages/8e/be/40b1bc2c3221acdefeb9dab6773d43cda7543ed0d8c8df8768f05af2d01e/cffi-1.11.5-cp36-cp36m-macosx_10_6_intel.whl
      Collecting asn1crypto>=0.21.0 (from cryptography>=2.2.1->pyOpenSSL->-r requirements.txt (line 2))
        Using cached https://files.pythonhosted.org/packages/ea/cd/35485615f45f30a510576f1a56d1e0a7ad7bd8ab5ed7cdc600ef7cd06222/asn1crypto-0.24.0-py2.py3-none-any.whl
      Collecting pycparser (from cffi!=1.11.3,>=1.7->cryptography>=2.2.1->pyOpenSSL->-r requirements.txt (line 2))
        Using cached https://files.pythonhosted.org/packages/68/9e/49196946aee219aead1290e00d1e7fdeab8567783e83e1b9ab5585e6206a/pycparser-2.19.tar.gz
      Installing collected packages: idna, urllib3, certifi, chardet, requests, six, pycparser, cffi, asn1crypto, cryptography, pyOpenSSL, pyasn1, ndg-httpsclient, tabulate, websocket-client, slackclient, pycrypto, simple-crypt
        Running setup.py install for pycparser ... done
        Running setup.py install for tabulate ... done
        Running setup.py install for pycrypto ... done
        Running setup.py install for simple-crypt ... done
      Successfully installed asn1crypto-0.24.0 certifi-2018.10.15 cffi-1.11.5 chardet-3.0.4 cryptography-2.4.2 idna-2.7 ndg-httpsclient-0.5.1 pyOpenSSL-18.0.0 pyasn1-0.4.4 pycparser-2.19 pycrypto-2.6.1 requests-2.20.1 simple-crypt-4.1.7 six-1.11.0 slackclient-1.3.0 tabulate-0.8.2 urllib3-1.24.1 websocket-client-0.54.0
      You are using pip version 9.0.1, however version 18.1 is available.
      You should consider upgrading via the 'pip install --upgrade pip' command.

      Setup complete.  To begin the lab run:

       source start
 ```
</details>

### Lab Startup
8. Run **`source start`** to prepare the workstation and to activate the pre-created Python virtual environment. <br />

<details>
     <summary>Sample Start Output</summary>

 ```concole
  Preparing the Workstation to Run this lab

  Note: This command script should be run with 'source start'
  to prepare the active terminal session.

  Activating Python Virtual Environment
  Opening Incognito browser windows for lab
 ```
</details>

9. To execute the script, copy and paste the following command in the terminal: <br />

     ```concole
     python interface-SpeedReport.py
      ```

## Configuration & Usage

10. Enter the following information to generate the report based on Cisco DNA Canter DevNet Sandbox environment: <br />

|Prompt   | Input |
|:-----|:-------------|
|IP Address | **`sandboxdnac.cisco.com`** |
|Username | **`devnetuser`** |
|Password | **`Cisco123!`** |

:warning: In case of typos, please click on "control C" to stop the script execution. After that, copy and paste `python interface-SpeedReport.py` to restart this exercise. <br />
:warning: It is recommended to expand the Terminal window to 160x70 for optimal view. <br />

An example of script execution: <br />
![alt text](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/newReport2.png)


## Script Overview
  * Prompt the user for Cisco DNA Center login information
![alt text](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/newReport3.png)<br />
  * Validate login information and get the Token key
![alt text](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/newReport4.png)<br />
  * Get the interfaces speed information and parse the date in a table format
![alt text](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/newReport5.png)<br />

## Technologies & Frameworks Used
### Cisco Products & Services:
  * Cisco DNA Center

### Tools & Frameworks:
  * This code requires Python 3.x
  * tabulate module

## Getting help & involved
Need help with the code? Got questions/concerns? Want to provide feedback? <br />
Please contact [Yossi Meloch](mailto:ymeloch@cisco.com) <br />

## Authors & Maintainers
:email: [Yossi Meloch](mailto:ymeloch@cisco.com) <br />
:email: [Stanley Chan](stanchan@cisco.com) <br />

## Licensing info
This project is licensed to you under the terms of the **[Cisco Sample Code License](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/LICENSE)**
