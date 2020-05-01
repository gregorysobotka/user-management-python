import sys
import argparse
from users.add import userByName

## Command Line Arguments ##
# --h (host)
# --u (user)
# --c (comment)

parser = argparse.ArgumentParser(description="Enter the username to be created")
parser.add_argument("--u", required=True, help="Please enter the username you are trying to create.")
parser.add_argument("--h", required=True, help="Please enter the target remote you are trying to reach.")
parser.add_argument("--c", default="", help="Enter the comments for the user.")
parser.add_argument("--pk", required=True, help="Please enter the public SSH key for this user.")
args = parser.parse_args()

# Host
host = args.h

# Comments 
comments = "\"" + args.c + "\""

# User Name
userName = args.u

# User Name
publicKey = args.pk

userByName(host, userName, comments, publicKey)