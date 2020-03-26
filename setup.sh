#! /bin/bash
echo " "
echo "Setting up the workstation environment for the lab."
echo " "

echo "Creating Python 3 Virtual Environment"
python3 -m venv venv
source venv/bin/activate
#pip install -r requirements.txt --ignore-installed six
pip install -r requirements.txt
echo " "

echo "Setup complete.  To begin the lab run: "
echo " "
echo " source start"
echo " "
