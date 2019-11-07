#!/bin/bash
wget http://tinycorelinux.net/10.x/x86/tcz/python3.6.tcz
wget https://raw.githubusercontent.com/IamEld3st/Wiperooni/master/wipe.py

echo "tce-load -i /home/tc/python3.6.tcz" > .profile
echo "python3 /home/tc/wipe.py" > .profile