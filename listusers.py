import sys
import argparse
from users.list import all

## Command Line Arguments ##
# --h (host)

parser = argparse.ArgumentParser(description="Enter the address of the remote in order to list users.")
parser.add_argument("--h", default="", required=True, help="Please enter the target remote you are trying to reach.")

args = parser.parse_args()

# Target Host
host = args.h

all(host)
