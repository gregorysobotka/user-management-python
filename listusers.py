import sys
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Enter the address of the remote in order to list users.')
parser.add_argument("--h", default="", help="Please enter the target remote you are trying to reach.")

args = parser.parse_args()

# Target Host
host = args.h

# Command to retrieve user fields 1,3,5 ( user name, user id, user comments field )
command = "cut -d : -f 1,3,5 /etc/passwd"

# Specify connection type (ssh), pem key location, remote, command to be passed 
connectionContext = ["ssh", host, command]

##
connection = subprocess.Popen(
    connectionContext, 
    shell=False, 
    universal_newlines=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)

try:
    response, err = connection.communicate(timeout=10)
    if err:
        print(err)
    else:
        print(response)
except:
    connection.kill()
    response, err = connection.communicate()
    print(err)