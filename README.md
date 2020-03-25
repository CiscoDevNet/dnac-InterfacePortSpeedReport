# Cisco DNA Center - Interfaces Speed (custom) Report

Ever wondered how to create a custom Cisco DNA Center report?  <br /> For example, "Get all Interfaces Ports Speed" report?  <br /> <br />
As part of this tutorial/repository, you will learn how to leverage the "Get All Interfaces" API call do build a custom/tailor-made report. <br />
The generated data can be then uploaded/integrated with cross-solutions such as Spark, Qlik, SmartSheet, and others.  <br />

![alt text](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/pics/story2.png) <br />

### Objectives and Flow
![alt text](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/pics/lab2Flow.png)

## Description

1. Let us start with reviewing the available DNA Center "Interfaces" API calls in **[Cisco documentation](https://developer.cisco.com/site/dna-center-rest-api/)** (Hint: Search for ***"Get all interfaces"*** under the ***"Devices"*** submenu). <br />

2. Right-click on the following GET API call to get in-depth information about all the available data types. <br />
<p align="center">
    <a href="https://developer.cisco.com/site/dna-center-rest-api/"><img src="https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/pics/newReport1.png" title="DNA Center API Calls" align="center" /></a>
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

5. Open a **Terminal** window (Press CMD + Space, type "Terminal" and hit return). <br />

6. Clone the code to your workstation (Copy & Paste the commands below). <br />

    ```concole
    cd /tmp
    git clone https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-.git
    cd dnac-InterfacePortSpeedReport
    ```

7. To execute the script, copy and paste the following command in the terminal: <br />

     ```concole
     python interface-SpeedReport.py
      ```
## Configuration & Usage

8. Enter the following information to generate the report based on Cisco DNA Canter DevNet Sandbox environment: <br />

|Prompt   | Input |
|:-----|:-------------|
|IP Address | **`sandboxdnac.cisco.com`** |
|Username | **`devnetuser`** |
|Password | **`Cisco123!`** |

:warning: In case of typos, please click on "control C" to stop the script execution. After that, copy and paste `python interface-SpeedReport.py` to restart this exercise. <br />
:warning: It is recommended to expand the Terminal window to 160x70 for optimal view. <br />

An example of script execution: <br />
![alt text](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/pics/newReport2.png)


## Script Overview
  * Prompt the user for Cisco DNA Center login information
![alt text](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/pics/newReport3.png)<br />
  * Validate login information and get the Token key
![alt text](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/pics/newReport4.png)<br />
  * Get the interfaces speed information and parse the date in a table format
![alt text](https://github.com/CiscoDevNet/dnac-InterfacePortSpeedReport-/blob/master/pics/newReport5.png)<br />

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
