from communication.remote import open

def all(host):

    # Command to retrieve user fields 1,3,5 ( user name, user id, user comments field )
    command = "cut -d : -f 1,3,5 /etc/passwd"

    # Specify connection type (ssh), pem key location, remote, command to be passed 
    connectionContext = ["ssh", host, command]

    open(connectionContext)