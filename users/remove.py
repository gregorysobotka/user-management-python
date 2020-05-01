from communication.remote import open

def userByName(host, userName):

    # Create User, User Home Directory
    deleteUserAndHomeDirCommand = "sudo userdel " + userName + " && sudo rm -r /home/" + userName

    # Specify connection type (ssh), pem key location, remote, command to be passed 
    connectionContext = ["ssh", host, deleteUserAndHomeDirCommand]

    open(connectionContext)