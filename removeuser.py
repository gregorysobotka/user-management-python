import sys
import subprocess
import argparse
from communication import remote
from users.remove import userByName

## Command Line Arguments ##
# --u (user)
# --h (host)

parser = argparse.ArgumentParser(description='Enter the username to be deleted')
parser.add_argument("--u", required=True, help="Please enter the username you are trying to delete.")
parser.add_argument("--h", required=True, help="Please enter the target remote you are trying to reach.")
args = parser.parse_args()

# User Name
userName = args.u

# Host
host = args.h

# 
userByName(host, userName)
