import sys
import subprocess
import argparse

parser = argparse.ArgumentParser(description='Enter the username to be deleted')
parser.add_argument("--u", default="", help="Please enter the username you are trying to delete.")
parser.add_argument("--h", default="", help="Please enter the target remote you are trying to reach.")
args = parser.parse_args()

# User Name
userName = args.u

# Host
host = args.h

# Create User, User Home Directory
deleteUserAndHomeDirCommand = "sudo userdel " + userName + " && sudo rm -r /home/" + userName

# Specify connection type (ssh), pem key location, remote, command to be passed 
connectionContext = ["ssh", host, deleteUserAndHomeDirCommand]

# connection = subprocess.Popen(connectionContext, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
connection = subprocess.Popen(
    connectionContext, 
    shell=False, 
    universal_newlines=True, 
    stdout=subprocess.PIPE, 
    stderr=subprocess.PIPE)

try:
    response, err = connection.communicate(timeout=10)
    print(err)
    print(response)
except:
    connection.kill()
    response, err = connection.communicate()
    print("Error: " + err)